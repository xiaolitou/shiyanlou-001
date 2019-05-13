from io import BytesIO

from sqlalchemy import func, Float, select, and_, desc
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from seiya.db import engine, Session, JobModel


def count_top10():
    """职位数排名前十的城市

    """
    session = Session()
    rows = session.query(
        JobModel.city,
        func.count(JobModel.city).label('count')
    ).group_by(JobModel.city).order_by(desc('count')).limit(10)
    return [row._asdict() for row in rows]


def salary_top10():
    """薪资排名前十的城市

    """
    session = Session()
    rows = session.query(
        JobModel.city,
        func.avg(
            (JobModel.salary_lower + JobModel.salary_upper) / 2
        ).label('salary')
    ).filter(
        and_(JobModel.salary_lower > 0, JobModel.salary_upper > 0)
    ).group_by(JobModel.city).order_by(desc('salary')).limit(10)
    薪资排名列表 = [row._asdict() for row in rows]  
    # 列表中每个元素是字典，字典的 salary 值的数据类型是 Decimal
    # 须将其转换为 float 类型
    for d in 薪资排名列表:
        d['salary'] = float(format(d['salary'], '.2f'))
    return 薪资排名列表


def _hot_tags():
    """热门职位标签
    使用 Pandas 从数据库表读取数据并进行分析

    返回结果类型为 [pandas.Series]
    """
    df = pd.read_sql(select([JobModel.tags]), engine)

    df = pd.concat([pd.Series(row['tags'].split(' ')) for _, row in df.iterrows()]).reset_index()
    del df['index']
    df.columns = ['tag']

    #df = df[df['tag'] != '""']
    #df = df[df['tag'] != '']

    return df.groupby(['tag']).size().sort_values(ascending=False)


def hot_tags():
    """热门职位标签

    返回结果类型为 [list]
    """
    rows = []
    for item in _hot_tags().items():
        #print('item: {}'.format(item))
        rows.append({'tag': item[0], 'count': item[1]})
    
    #print('rows: {}'.format(rows))
    return rows


def hot_tags_plot(format='png'):
    """热门职位标签

    返回结果类型为图片
    """

    #mpl.rcParams['font.family'] = ['serif']
    #mpl.rcParams['font.serif'] = ['SimHei']
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rcParams['figure.figsize'] = 10, 5

    s = _hot_tags()

    plt.bar(s.index[:10], s.values[:10])

    img = BytesIO()
    plt.savefig(img, format=format)

    return img.getvalue()


def experience_stat():
    """工作经验统计

    """
    session = Session()
    rows = session.query(
        func.concat(
            JobModel.experience_lower, '-', JobModel.experience_upper, '年'
        ).label('experience'),
        func.count('experience').label('count')
    ).group_by('experience').order_by(desc('count'))
    return [row._asdict() for row in rows]


def education_stat():
    """学历要求统计

    """
    session = Session()
    rows = session.query(
        JobModel.education,
        func.count(JobModel.education).label('count')
    ).group_by('education').order_by(desc('count'))
    学历要求统计 = [row._asdict() for row in rows]
    return 学历要求统计


def salary_by_city_and_education():
    """同等学历不同城市薪资对比

    """
    session = Session()
    rows = session.query(
        JobModel.city,
        JobModel.education,
        func.avg(
            (JobModel.salary_lower + JobModel.salary_upper) / 2
        ).cast(Float).label('salary')
    ).filter(
        and_(JobModel.salary_lower > 0, JobModel.salary_upper > 0)
    ).group_by(JobModel.city, JobModel.education).order_by(JobModel.city.desc())
    #return [row._asdict() for row in rows]
    同等学历不同城市薪资对比 = [row._asdict() for row in rows]
    for i in 同等学历不同城市薪资对比:
        i['salary'] = float(format(i['salary'],'.2f'))
    return 同等学历不同城市薪资对比
