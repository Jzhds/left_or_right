import pandas as pd
import numpy as np


class Scoring:
    '''
    对基金的前瞻性进行打分
    '''
    def __init__(self,data,fund_name):
        '''

        :param fund_name: 基金的wind代码
        :param data:包含所有基金情况的数据框
        '''
        self.fund_name = fund_name
        self.data = data

    @property
    def timing_score( self ):
        '''

        :return: 根据持仓时间在同业中的排名对基金的前瞻性进行打分,采取5分制，排名越高，分数越高
        '''
        timing_rank = self.data.loc[self.fund_name,self.data.columns[-3]]
        #根据data_clean_and_analyeze中计算出的分位数进行判断打分
        if timing_rank<7.41:
            temp_score = 5
        elif timing_rank<25.06:
            temp_score = 4
        elif timing_rank<49.4:
            temp_score = 3
        elif timing_rank<77.87:
            temp_score = 2
        else:
            temp_score = 1
        return temp_score

    @property
    def unique_score( self ):
        '''

        :return: 根据持仓股票的持有基金数衡量基金选股的独特性，对基金的前瞻性进行打分,采取5分制，重仓股票持有的基金数越少，分数越高
        '''
        timing_rank = self.data.loc[self.fund_name, '重仓股票平均持仓基金数']
        # 根据data_clean_and_analyeze中计算出的分位数进行判断打分
        if timing_rank < 98.4:
            temp_score = 5
        elif timing_rank < 299.6:
            temp_score = 4
        elif timing_rank < 507.2:
            temp_score = 3
        elif timing_rank < 910:
            temp_score = 2
        else:
            temp_score = 1
        return temp_score

    @property
    def anti_trend_score( self ):
        '''

        :return: 根据持仓股票的过去两个月的涨跌幅，对基金的前瞻性进行打分,采取5分制，涨幅越低，分数越高
        '''
        timing_rank = self.data.loc[self.fund_name, '重仓股票平均涨跌幅']
        # 根据data_clean_and_analyeze中计算出的分位数进行判断打分
        if timing_rank < 11.42:
            temp_score = 5
        elif timing_rank < 17.5:
            temp_score = 4
        elif timing_rank < 20.9:
            temp_score = 3
        elif timing_rank < 30.06:
            temp_score = 2
        else:
            temp_score = 1
        return temp_score

    def summary( self ):
        '''

        :return: 根据上面的不同角度的得分对基金的前瞻性进行汇总，并评价判断基金市前瞻性投资还是趋势性投资
        '''
        timing_score = self.timing_score
        unique_score = self.unique_score
        anti_trend_score =  self.anti_trend_score
        total_score = np.mean([timing_score,unique_score,anti_trend_score])
        trend_score = 5 -  total_score
        print(f"{self.fund_name}情况汇总:")
        print(f"持仓时间方面前瞻性投资得分为{timing_score}\n"
              f"持仓股票独特性方面前瞻性投资得分为{unique_score}\n"
              f"逆趋势方面前瞻性投资得分为{anti_trend_score}\n"
              f"前瞻性投资得分为{total_score}\n"
              f"趋势性投资得分为{trend_score}"
              )
        if trend_score<2.5:
            print("为前瞻性投资")
        else:
            print("为趋势性投资")
        return total_score




if __name__ == '__main__':
    data = pd.read_excel("cleaned_data.xlsx",index_col=0)
    left_score = Scoring(data=data,fund_name='001166.OF').summary()
