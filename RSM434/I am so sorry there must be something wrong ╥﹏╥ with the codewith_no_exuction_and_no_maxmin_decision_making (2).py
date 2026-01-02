import requests
from time import sleep
import numpy as np

s = requests.Session()
s.headers.update({'X-API-key': '31K6K3GF'})

def get_tick():
    resp = s.get('http://localhost:9999/v1/case')
    if resp.ok:
        case = resp.json()
        return case['tick'], case['status']
  
def get_news(eps_estimates, ownership_estimates, eps, Lower_eps_estimates, Higher_ownership_estimates, Lower_ownership_estimates, tick):
    resp = s.get ('http://localhost:9999/v1/news', params = {'limit': 50}) # default limit is 20
    if resp.ok:
        news_query = resp.json()
        
        for i in news_query[::-1]: # iterating backwards through the list, news items are ordered newest to oldest         

            if i['headline'].find("TP") > -1:
    
                if i['headline'].find("Analyst") > -1:
                    
                    if i['headline'].find("#1") > -1:
                        eps_estimates[0, 0] = float(i['body'][i['body'].find("Q1:") + 5 : i['body'].find("Q1:") + 9 ])
                        eps_estimates[0, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[0, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[0, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])
                        
                        if tick >= 0 and tick < 40:
                            Lower_eps_estimates[0, 0] = eps_estimates[0, 0] - 0.02 * (1 - 0)
                            Lower_eps_estimates[0, 1] = eps_estimates[0, 1] - 0.02 * (2 - 0)
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 0)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 0)
                        elif tick >= 40 and tick < 100:
                            Lower_eps_estimates[0, 1] = eps_estimates[0, 1] - 0.02 * (2 - 1)
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 1)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 2)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 3)
                        
                    if i['headline'].find("#2") > -1:
                        eps_estimates[0, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[0, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[0, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 40 and tick < 100:
                            Lower_eps_estimates[0, 1] = eps_estimates[0, 1] - 0.02 * (2 - 1)
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 1)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 2)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 3)

                    if i['headline'].find("#3") > -1:
                        eps_estimates[0, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[0, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 100 and tick < 160:
                            Lower_eps_estimates[0, 2] = eps_estimates[0, 2] - 0.02 * (3 - 2)
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 3)

                    if i['headline'].find("#4") > -1:
                        eps_estimates[0, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 160 and tick < 220:
                            Lower_eps_estimates[0, 3] = eps_estimates[0, 3] - 0.02 * (4 - 3)
                    
                if i['headline'].find("institutional") > -1:
                    
                    if i['headline'].find("Q1") > -1:
                        ownership_estimates[0, 0] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[0, 0] = ownership_estimates[0, 0] - (0.20 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[0, 0] = ownership_estimates[0, 0] + (0.20 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[0, 0] = ownership_estimates[0, 0] - (0.20 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[0, 0] = ownership_estimates[0, 0] + (0.20 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[0, 0] = ownership_estimates[0, 0] - (0.20 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[0, 0] = ownership_estimates[0, 0] + (0.20 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[0, 0] = ownership_estimates[0, 0] - (0.20 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[0, 0] = ownership_estimates[0, 0] + (0.20 - (3 - 3) * 0.05)
                    
                    if i['headline'].find("Q2") > -1:
                        ownership_estimates[0, 1] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[0, 1] = ownership_estimates[0, 1] - (0.20 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[0, 1] = ownership_estimates[0, 1] + (0.20 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[0, 1] = ownership_estimates[0, 1] - (0.20 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[0, 1] = ownership_estimates[0, 1] + (0.20 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[0, 1] = ownership_estimates[0, 1] - (0.20 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[0, 1] = ownership_estimates[0, 1] + (0.20 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[0, 1] = ownership_estimates[0, 1] - (0.20 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[0, 1] = ownership_estimates[0, 1] + (0.20 - (3 - 3) * 0.05)

                    if i['headline'].find("Q3") > -1:
                        ownership_estimates[0, 2] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                                            
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[0, 2] = ownership_estimates[0, 2] - (0.20 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[0, 2] = ownership_estimates[0, 2] + (0.20 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[0, 2] = ownership_estimates[0, 2] - (0.20 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[0, 2] = ownership_estimates[0, 2] + (0.20 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[0, 2] = ownership_estimates[0, 2] - (0.20 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[0, 2] = ownership_estimates[0, 2] + (0.20 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[0, 2] = ownership_estimates[0, 2] - (0.20 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[0, 2] = ownership_estimates[0, 2] + (0.20 - (3 - 3) * 0.05)

                    if i['headline'].find("Q4") > -1:
                        ownership_estimates[0, 3] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[0, 3] = ownership_estimates[0, 3] - (0.20 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[0, 3] = ownership_estimates[0, 3] + (0.20 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[0, 3] = ownership_estimates[0, 3] - (0.20 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[0, 3] = ownership_estimates[0, 3] + (0.20 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[0, 3] = ownership_estimates[0, 3] - (0.20 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[0, 3] = ownership_estimates[0, 3] + (0.20 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[0, 3] = ownership_estimates[0, 3] - (0.20 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[0, 3] = ownership_estimates[0, 3] + (0.20 - (3 - 3) * 0.05)
                
            if i['headline'].find("AS") > -1:
                
                if i['headline'].find("Analyst") > -1:
                    
                    if i['headline'].find("#1") > -1:
                        eps_estimates[1, 0] = float(i['body'][i['body'].find("Q1:") + 5 : i['body'].find("Q1:") + 9 ])
                        eps_estimates[1, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[1, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[1, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])
                        
                        if tick >= 0 and tick < 40:
                            Lower_eps_estimates[1, 0] = eps_estimates[1, 0] - 0.04 * (1 - 0)
                            Lower_eps_estimates[1, 1] = eps_estimates[1, 1] - 0.04 * (2 - 0)
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 0)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 0)
                        elif tick >= 40 and tick < 100:
                            Lower_eps_estimates[1, 1] = eps_estimates[1, 1] - 0.04 * (2 - 1)
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 1)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 2)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 3)
                        
                    if i['headline'].find("#2") > -1:
                        eps_estimates[1, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[1, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[1, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 40 and tick < 100:
                            Lower_eps_estimates[1, 1] = eps_estimates[1, 1] - 0.04 * (2 - 1)
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 1)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 2)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 3)

                    if i['headline'].find("#3") > -1:
                        eps_estimates[1, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[1, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 100 and tick < 160:
                            Lower_eps_estimates[1, 2] = eps_estimates[1, 2] - 0.04 * (3 - 2)
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 3)

                    if i['headline'].find("#4") > -1:
                        eps_estimates[1, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 160 and tick < 220:
                            Lower_eps_estimates[1, 3] = eps_estimates[1, 3] - 0.04 * (4 - 3)
                    
                if i['headline'].find("institutional") > -1:
                    
                    if i['headline'].find("Q1") > -1:
                        ownership_estimates[1, 0] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[1, 0] = ownership_estimates[1, 0] - (0.25 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[1, 0] = ownership_estimates[1, 0] + (0.25 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[1, 0] = ownership_estimates[1, 0] - (0.25 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[1, 0] = ownership_estimates[1, 0] + (0.25 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[1, 0] = ownership_estimates[1, 0] - (0.25 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[1, 0] = ownership_estimates[1, 0] + (0.25 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[1, 0] = ownership_estimates[1, 0] - (0.25 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[1, 0] = ownership_estimates[1, 0] + (0.25 - (3 - 3) * 0.05)
                    
                    if i['headline'].find("Q2") > -1:
                        ownership_estimates[1, 1] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[1, 1] = ownership_estimates[1, 1] - (0.25 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[1, 1] = ownership_estimates[1, 1] + (0.25 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[1, 1] = ownership_estimates[1, 1] - (0.25 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[1, 1] = ownership_estimates[1, 1] + (0.25 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[1, 1] = ownership_estimates[1, 1] - (0.25 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[1, 1] = ownership_estimates[1, 1] + (0.25 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[1, 1] = ownership_estimates[1, 1] - (0.25 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[1, 1] = ownership_estimates[1, 1] + (0.25 - (3 - 3) * 0.05)

                    if i['headline'].find("Q3") > -1:
                        ownership_estimates[1, 2] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                                            
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[1, 2] = ownership_estimates[1, 2] - (0.25 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[1, 2] = ownership_estimates[1, 2] + (0.25 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[1, 2] = ownership_estimates[1, 2] - (0.25 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[1, 2] = ownership_estimates[1, 2] + (0.25 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[1, 2] = ownership_estimates[1, 2] - (0.25 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[1, 2] = ownership_estimates[1, 2] + (0.25 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[1, 2] = ownership_estimates[1, 2] - (0.25 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[1, 2] = ownership_estimates[1, 2] + (0.25 - (3 - 3) * 0.05)

                    if i['headline'].find("Q4") > -1:
                        ownership_estimates[1, 3] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[1, 3] = ownership_estimates[1, 3] - (0.25 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[1, 3] = ownership_estimates[1, 3] + (0.25 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[1, 3] = ownership_estimates[1, 3] - (0.25 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[1, 3] = ownership_estimates[1, 3] + (0.25 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[1, 3] = ownership_estimates[1, 3] - (0.25 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[1, 3] = ownership_estimates[1, 3] + (0.25 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[1, 3] = ownership_estimates[1, 3] - (0.25 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[1, 3] = ownership_estimates[1, 3] + (0.25 - (3 - 3) * 0.05)
                
            if i['headline'].find("BA") > -1:
                
                if i['headline'].find("Analyst") > -1:
                    
                    if i['headline'].find("#1") > -1:
                        eps_estimates[2, 0] = float(i['body'][i['body'].find("Q1:") + 5 : i['body'].find("Q1:") + 9 ])
                        eps_estimates[2, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[2, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[2, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])
                        
                        if tick >= 0 and tick < 40:
                            Lower_eps_estimates[2, 0] = eps_estimates[2, 0] - 0.06 * (1 - 0)
                            Lower_eps_estimates[2, 1] = eps_estimates[2, 1] - 0.06 * (2 - 0)
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 0)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 0)
                        elif tick >= 40 and tick < 100:
                            Lower_eps_estimates[2, 1] = eps_estimates[2, 1] - 0.06 * (2 - 1)
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 1)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 2)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 3)
                        
                    if i['headline'].find("#2") > -1:
                        eps_estimates[2, 1] = float(i['body'][i['body'].find("Q2:") + 5 : i['body'].find("Q2:") + 9 ])
                        eps_estimates[2, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[2, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 40 and tick < 100:
                            Lower_eps_estimates[2, 1] = eps_estimates[2, 1] - 0.06 * (2 - 1)
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 1)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 1)
                        elif tick >= 100 and tick < 160:
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 2)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 3)

                    if i['headline'].find("#3") > -1:
                        eps_estimates[2, 2] = float(i['body'][i['body'].find("Q3:") + 5 : i['body'].find("Q3:") + 9 ])
                        eps_estimates[2, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 100 and tick < 160:
                            Lower_eps_estimates[2, 2] = eps_estimates[2, 2] - 0.06 * (3 - 2)
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 2)
                        elif tick >= 160 and tick < 220:
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 3)

                    if i['headline'].find("#4") > -1:
                        eps_estimates[2, 3] = float(i['body'][i['body'].find("Q4:") + 5 : i['body'].find("Q4:") + 9 ])

                        if tick >= 160 and tick < 220:
                            Lower_eps_estimates[2, 3] = eps_estimates[2, 3] - 0.06 * (4 - 3)
                    
                if i['headline'].find("institutional") > -1:
                    
                    if i['headline'].find("Q1") > -1:
                        ownership_estimates[2, 0] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[2, 0] = ownership_estimates[2, 0] - (0.30 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[2, 0] = ownership_estimates[2, 0] + (0.30 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[2, 0] = ownership_estimates[2, 0] - (0.30 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[2, 0] = ownership_estimates[2, 0] + (0.30 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[2, 0] = ownership_estimates[2, 0] - (0.30 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[2, 0] = ownership_estimates[2, 0] + (0.30 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[2, 0] = ownership_estimates[2, 0] - (0.30 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[2, 0] = ownership_estimates[2, 0] + (0.30 - (3 - 3) * 0.05)
                    
                    if i['headline'].find("Q2") > -1:
                        ownership_estimates[2, 1] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[2, 1] = ownership_estimates[2, 1] - (0.30 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[2, 1] = ownership_estimates[2, 1] + (0.30 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[2, 1] = ownership_estimates[2, 1] - (0.30 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[2, 1] = ownership_estimates[2, 1] + (0.30 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[2, 1] = ownership_estimates[2, 1] - (0.30 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[2, 1] = ownership_estimates[2, 1] + (0.30 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[2, 1] = ownership_estimates[2, 1] - (0.30 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[2, 1] = ownership_estimates[2, 1] + (0.30 - (3 - 3) * 0.05)

                    if i['headline'].find("Q3") > -1:
                        ownership_estimates[2, 2] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                                            
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[2, 2] = ownership_estimates[2, 2] - (0.30 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[2, 2] = ownership_estimates[2, 2] + (0.30 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[2, 2] = ownership_estimates[2, 2] - (0.30 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[2, 2] = ownership_estimates[2, 2] + (0.30 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[2, 2] = ownership_estimates[2, 2] - (0.30 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[2, 2] = ownership_estimates[2, 2] + (0.30 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[2, 2] = ownership_estimates[2, 2] - (0.30 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[2, 2] = ownership_estimates[2, 2] + (0.30 - (3 - 3) * 0.05)

                    if i['headline'].find("Q4") > -1:
                        ownership_estimates[2, 3] = float(i['body'][i['body'].find("%") - 5 : i['body'].find("%")])                                    
                        if tick >= 0 and tick < 70:
                            Lower_ownership_estimates[2, 3] = ownership_estimates[2, 3] - (0.30 - (3 - 0) * 0.05)
                            Higher_ownership_estimates[2, 3] = ownership_estimates[2, 3] + (0.30 - (3 - 0) * 0.05)
                        elif tick >= 70 and tick < 130:
                            Lower_ownership_estimates[2, 3] = ownership_estimates[2, 3] - (0.30 - (3 - 1) * 0.05)
                            Higher_ownership_estimates[2, 3] = ownership_estimates[2, 3] + (0.30 - (3 - 1) * 0.05)
                        elif tick >= 130 and tick < 190:
                            Lower_ownership_estimates[2, 3] = ownership_estimates[2, 3] - (0.30 - (3 - 2) * 0.05)
                            Higher_ownership_estimates[2, 3] = ownership_estimates[2, 3] + (0.30 - (3 - 2) * 0.05)
                        elif tick >= 190 and tick < 250:
                            Lower_ownership_estimates[2, 3] = ownership_estimates[2, 3] - (0.30 - (3 - 3) * 0.05)
                            Higher_ownership_estimates[2, 3] = ownership_estimates[2, 3] + (0.30 - (3 - 3) * 0.05)
                
            if i['headline'].find("Earnings release") > -1:
                                    
                if i['headline'].find("Q1") > -1:
                    eps[0, 0] = float(i['body'][i['body'].find("TP Q1:") + 32 : i['body'].find("TP Q1:") + 36 ])
                    eps[1, 0] = float(i['body'][i['body'].find("AS Q1:") + 32 : i['body'].find("AS Q1:") + 36 ])
                    eps[2, 0] = float(i['body'][i['body'].find("BA Q1:") + 32 : i['body'].find("BA Q1:") + 36 ])
                    
                if i['headline'].find("Q2") > -1:
                    eps[0, 1] = float(i['body'][i['body'].find("TP Q2:") + 32 : i['body'].find("TP Q2:") + 36 ])
                    eps[1, 1] = float(i['body'][i['body'].find("AS Q2:") + 32 : i['body'].find("AS Q2:") + 36 ])
                    eps[2, 1] = float(i['body'][i['body'].find("BA Q2:") + 32 : i['body'].find("BA Q2:") + 36 ])

                if i['headline'].find("Q3") > -1:
                    eps[0, 2] = float(i['body'][i['body'].find("TP Q3:") + 32 : i['body'].find("TP Q3:") + 36 ])
                    eps[1, 2] = float(i['body'][i['body'].find("AS Q3:") + 32 : i['body'].find("AS Q3:") + 36 ])
                    eps[2, 2] = float(i['body'][i['body'].find("BA Q3:") + 32 : i['body'].find("BA Q3:") + 36 ])

                if i['headline'].find("Q4") > -1:
                    eps[0, 3] = float(i['body'][i['body'].find("TP Q4:") + 32 : i['body'].find("TP Q4:") + 36 ])
                    eps[1, 3] = float(i['body'][i['body'].find("AS Q4:") + 32 : i['body'].find("AS Q4:") + 36 ])
                    eps[2, 3] = float(i['body'][i['body'].find("BA Q4:") + 32 : i['body'].find("BA Q4:") + 36 ])
                                
        return eps_estimates, ownership_estimates, eps, Lower_eps_estimates, Higher_ownership_estimates, Lower_ownership_estimates           


def main():
    
    tick, status = get_tick()
    
    eps_estimates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    eps_estimates = eps_estimates.reshape(3,4)
    
    ownership_estimates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    ownership_estimates = ownership_estimates.reshape(3,4)
    
    eps = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    eps = eps.reshape(3,4)
    
    eps_val = np.array([0.40, 0.33, 0.33, 0.37, 0.35, 0.45, 0.50, 0.25, 0.15, 0.50, 0.60, 0.25])
    eps_val = eps_val.reshape(3,4)
    
    lower_eps_val = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    lower_eps_val = lower_eps_val.reshape(3,4)
    
    higher_own_val = np.array([0.0, 0.0, 0.0])
    higher_own_val = higher_own_val.reshape(3,1)
    
    lower_own_val = np.array([0.0, 0.0, 0.0])
    lower_own_val = lower_own_val.reshape(3,1)
    
    Lower_eps_estimates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    Lower_eps_estimates = Lower_eps_estimates.reshape(3,4)
    
    Higher_ownership_estimates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    Higher_ownership_estimates = Higher_ownership_estimates.reshape(3,4)
    
    Lower_ownership_estimates = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    Lower_ownership_estimates = Lower_ownership_estimates.reshape(3,4)
    
    while status == "ACTIVE":
            
        eps_estimates, ownership_estimates, eps, Lower_eps_estimates, Higher_ownership_estimates, Lower_ownership_estimates = get_news(eps_estimates, ownership_estimates, eps, Lower_eps_estimates, Higher_ownership_estimates, Lower_ownership_estimates, tick)
        
        print("--- EPS Estimates ---")
        print(eps_estimates)
        print("--- Ownership Estimates ---")
        print(ownership_estimates)
        print("--- EPS ---")
        print(eps)
        print("--- Lower EPS Estimates ---")
        print(Lower_eps_estimates)
        print("--- Higher Ownership Estimates ---")
        print(Higher_ownership_estimates)
        print("--- Lower Ownership Estimates ---")
        print(Lower_ownership_estimates)
        
        # Update eps_val and lower_eps_val based on estimates
        for i in range(3):
            for j in range(4):
                if eps_estimates[i, j] != 0:
                    eps_val[i, j] = eps_estimates[i, j]
                if Lower_eps_estimates[i, j] != 0:
                    lower_eps_val[i, j] = Lower_eps_estimates[i, j]
                if ownership_estimates[i, j] != 0:
                    higher_own_val[i, 0] = Higher_ownership_estimates[i, j]
                    lower_own_val[i, 0] = Lower_ownership_estimates[i, j]
                if eps[i, j] != 0:
                    eps_val[i, j] = eps[i, j]
                    
        print("--- EPS for Valuation ---")
        print(eps_val)
        print("--- Lower EPS for Valuation ---")
        print(lower_eps_val)
        print("--- Higher Ownership for Valuation ---")
        print(higher_own_val)
        print("--- Lower Ownership for Valuation ---")
        print(lower_own_val)

        # Calculate conservative EPS estimates (min part of max-min function)
        TP_eps = lower_eps_val.sum(axis=1)[0]  # Sum of lower EPS estimates for TP
        AS_eps = lower_eps_val.sum(axis=1)[1]  # Sum of lower EPS estimates for AS
        BA_eps = lower_eps_val.sum(axis=1)[2]  # Sum of lower EPS estimates for BA

        # DDM and P/E Valuation for TP
        TP_g = (TP_eps / 1.43) - 1  # Growth rate for TP
        TP_div = TP_eps * 0.80  # Dividend for TP
        TP_DDM = ((TP_div * (1 + TP_g)) / (0.05 - TP_g)) * (1 - ((1 + TP_g) / (1 + 0.05))**5) + ((TP_div * ((1 + TP_g)**5) * (1 + 0.02)) / (0.05 - 0.02)) / (1 + 0.05)**5
        TP_pe = TP_eps * 12  # P/E valuation for TP

        # Decision making for TP valuation
        if TP_DDM > TP_pe:
            TP_val = (higher_own_val[0, 0] / 100) * TP_DDM + (1 - (higher_own_val[0, 0] / 100)) * TP_pe  # Use higher ownership estimate
            print("--- TP Valuation (DDM > PE, using Higher Ownership Estimate) ---")
        else:
            TP_val = (lower_own_val[0, 0] / 100) * TP_DDM + (1 - (lower_own_val[0, 0] / 100)) * TP_pe  # Use lower ownership estimate
            print("--- TP Valuation (DDM < PE, using Lower Ownership Estimate) ---")

        # DDM and P/E Valuation for AS
        AS_g = (AS_eps / 1.55) - 1  # Growth rate for AS
        AS_div = AS_eps * 0.50  # Dividend for AS
        AS_DDM = ((AS_div * (1 + AS_g)) / (0.075 - AS_g)) * (1 - ((1 + AS_g) / (1 + 0.075))**5) + ((AS_div * ((1 + AS_g)**5) * (1 + 0.02)) / (0.075 - 0.02)) / (1 + 0.075)**5
        AS_pe = AS_eps * 16  # P/E valuation for AS

        # Decision making for AS valuation
        if AS_DDM > AS_pe:
            AS_val = (higher_own_val[1, 0] / 100) * AS_DDM + (1 - (higher_own_val[1, 0] / 100)) * AS_pe  # Use higher ownership estimate
            print("--- AS Valuation (DDM > PE, using Higher Ownership Estimate) ---")
        else:
            AS_val = (lower_own_val[1, 0] / 100) * AS_DDM + (1 - (lower_own_val[1, 0] / 100)) * AS_pe  # Use lower ownership estimate
            print("--- AS Valuation (DDM < PE, using Lower Ownership Estimate) ---")

        # DDM and P/E Valuation for BA
        BA_g = (BA_eps / 1.50) - 1  # Growth rate for BA
        BA_pe_inst = 20 * (1 + BA_g) * BA_eps  # Institutional P/E valuation for BA
        BA_pe_retail = BA_eps * 20  # Retail P/E valuation for BA

        # Decision making for BA valuation
        if BA_pe_inst > BA_pe_retail:
            BA_val = (higher_own_val[2, 0] / 100) * BA_pe_inst + (1 - (higher_own_val[2, 0] / 100)) * BA_pe_retail  # Use higher ownership estimate
            print("--- BA Valuation (DDM > PE, using Higher Ownership Estimate) ---")
        else:
            BA_val = (lower_own_val[2, 0] / 100) * BA_pe_inst + (1 - (lower_own_val[2, 0] / 100)) * BA_pe_retail  # Use lower ownership estimate
            print("--- BA Valuation (DDM < PE, using Lower Ownership Estimate) ---")

        # Print final valuations
        print("--- TP Valuation ---")
        print(TP_val)
        print("--- AS Valuation ---")
        print(AS_val)
        print("--- BA Valuation ---")
        print(BA_val)
        
        sleep(0.5)
        tick, status = get_tick()
    
if __name__ == '__main__':
    main()