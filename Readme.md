### 投资是具有前瞻性 or 趋势性

#### 1.思路

（1）看投资持仓的持仓时间，持仓时间比较长的话，应该大概率是前瞻性投资

（2）新持仓的股票过去一段时间的趋势增长，增长比较多的话，可能是趋势性投资

（3）特异度：如果和其他基金经理持仓很一致的话，大概率是趋势性抱团，如果比较具有独特性，那么应该是具有前瞻性的

（4）股票估值水平的历史分位数：如果是在比较高的话，是趋势性，如果是在比较低的话，可能是前瞻性的（因为量化接口出了些问题，这个指标没有提取到）

#### 2.数据提取

（1）选择的基金范围为股票型开放式基金

![image-20210123100523791](https://i.loli.net/2021/01/23/SKAgcJhdkraYmNX.png)

（2）提取基金在2020年度的前五重仓股票的wind代码，2020年末披露的前五重仓股票的11-12月的区间涨跌幅，重仓股票的持有基金数，基金持有股票的平均持仓时间及其在同类基金重的排名

#### 3.代码逻辑

（1）data_clean_and_analyze：

对原数据进行初步的处理和分析，计算得到基金重仓股票的平均持仓基金数，重仓股票的平均涨跌幅，并计算对应列相应的20%，40%，60%，80%分位数，便于后面评分，并把处理后的数据输出到新的文件中

（2）fund_manager_scoring:

对基金的前瞻性进行打分，分为三个子维度，每个子维度的打分范围为1-5分

1.timing_score:根据持仓时间在同业中的排名对基金的前瞻性进行打分，持仓时间排名越高，分数越高

2.unique_score：根据持仓股票的持有基金数衡量基金选股的独特性，对基金的前瞻性进行打分，重仓股票持有的基金数越少，分数越高

3.anti_trend_score：根据持仓股票的过去两个月的涨跌幅，对基金的前瞻性进行打分,采取5分制，涨幅越低，分数越高

最后把三个维度的打分进行平均，得到前瞻性打分，趋势性打分为5-前瞻性打分。前瞻性打分趋势性打分两者较高者，判断该基金投资性质为该类。

