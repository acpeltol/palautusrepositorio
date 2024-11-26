class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):

        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1


    def tie_score_text(self,score):

        return_text = ["Love-All","Fifteen-All", "Thirty-All","Deuce"]

        try:
            score = return_text[self.m_score1]
        except:
            score = return_text[-1]

        return score
    
    def score_is_more_than_four_text(self, score):
        diffrence = self.m_score1 - self. m_score2

        return_text = ["Advantage player1","Win for player1","Win for player2","Advantage player2"]

        if diffrence == 1:
            score = return_text[diffrence - 1]
        elif diffrence == -1:
            score = return_text[diffrence]
        elif diffrence >= 2:
            score = return_text[1]
        else:
            score = return_text[2]

        return score
    
    def else_score_text(self,score,temp_score):

        return_texts = ["Love","Fifteen", "Thirty", "Forty"]

        temp_score = self.m_score1

        score += return_texts[temp_score]     
        score += "-"

        temp_score = self.m_score2

        score += return_texts[temp_score]

        return score

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            
            score = self.tie_score_text(score)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            
            score = self.score_is_more_than_four_text(score)

        else:
            
            score = self.else_score_text(score, temp_score)


        return score
