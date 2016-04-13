import matplotlib.pyplot as plt
from pylab import *
import numpy as np
twentyfive_sludge=0
fifty_sludge=0
seventyfive_sludge=0
raw_sludge=0
dict_substrates={}
dict_real_production={}
def theoretical_thermo_biogas_substrates_heat_pretreatment_FM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=12.81
    dict_substrates={'Slaughterhouse waste': 297.16, "Miscanthus Giganteus": 248.73, "Wheat Straw":320.24, "Maize silage": 290.60}
    dict_real_production={'Slaughterhouse waste': 82.36, "Miscanthus Giganteus": 43.46, "Wheat Straw":99.96, "Maize silage":83.96}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL THERMOPHILIC BIOGAS PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL THERMOPHILIC BIOGAS PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+100])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Fressh matter biogas production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", FRESH MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()

def theoretical_thermo_biogas_substrates_heat_pretreatment_ODM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=293.77
    dict_substrates={'Slaughterhouse waste': 978.20, "Miscanthus Giganteus": 295.96, "Wheat Straw":478.48, "Maize silage":790.52}
    dict_real_production={'Slaughterhouse waste': 800.58, "Miscanthus Giganteus": 177.83, "Wheat Straw":416.13, "Maize silage":676.62}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL THERMOPHILIC BIOGAS PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL THERMOPHILIC BIOGAS PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+200])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Organic dry matter biogas production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", ORGANIC DRY MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()

def theoretical_thermo_methane_substrates_heat_pretreatment_FM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=6.75
    dict_substrates={'Slaughterhouse waste': 198.93, "Miscanthus Giganteus": 133.39, "Wheat Straw":169.45, "Maize silage":153.24}
    dict_real_production={'Slaughterhouse waste': 50.96, "Miscanthus Giganteus": 20.89, "Wheat Straw":53.72, "Maize silage":43.49}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL THERMOPHILIC METHANE PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL THERMOPHILIC METHANE PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF FRESH MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        plt.ylim([0,dict_substrates[i]+100])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Fresh matter methane production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", FRESH MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        plt.legend()
        grid(True)
        show()       
        

def theoretical_thermo_methane_substrates_heat_pretreatment_ODM(raw_sludge, dict_substrates, dict_real_production):
    raw_sludge=154.75
    dict_substrates={'Slaughterhouse waste': 654.86, "Miscanthus Giganteus": 158.72, "Wheat Straw":253.19, "Maize silage":416.87}
    dict_real_production={'Slaughterhouse waste': 495.47, "Miscanthus Giganteus": 85.49, "Wheat Straw":222.80, "Maize silage":350.48}
    #It creates a list of theoretical biogas efficiencies from the production of the 
    #raw sludge and the production of the substrates without sludge, and compares it with the real production of the mixture
    #Everything in terms of Fresh Matter
    for i in dict_substrates:
        print " "
        print "THEORETICAL THERMOPHILIC METHANE PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER"
        print " "
        twentyfive_sludge=0.25*raw_sludge+0.75*dict_substrates[i]
        fifty_sludge=0.5*raw_sludge+0.5*dict_substrates[i]
        seventyfive_sludge=0.75*raw_sludge+0.25*dict_substrates[i]
        print "The production of 100% of sewage sludge is: " + str(raw_sludge) + "[m3/t f.m.]"
        print "|The theoretical production of 75% of sewage sludge and 25% of " + i + " is " + str(seventyfive_sludge) + "[m3/t f.m.]" + "|"      
        print "|The theoretical production of 50% of sewage sludge and 50% of " + i + " is " + str(fifty_sludge)+ "[m3/t f.m.]"+ "|" 
        print "|The theoretical production of 25% of sewage sludge and 75% of " + i + " is " + str(twentyfive_sludge)+ "[m3/t f.m.]"+ "|" 
        print "The production of 100% of " + i + " is " + str(dict_substrates[i])+ "[m3/t f.m.]"
        print "And the real production of 75% of sewage sludge and 25% of " + i + " was " + str(dict_real_production[i])+ "[m3/t f.m.]"
        sinergy=((dict_real_production[i]-seventyfive_sludge)/dict_real_production[i])*100
        print "The observed sinergy effect of mixing sewage sludge with " + i + " was: " + str(round (sinergy,2)) + "%"
        plt.figure("THEORETICAL THERMOPHILIC METHANE PRODUCTION WITH HEAT PRETREATMENT OF SEWAGE SLUDGE MIXED WITH " + i.upper() + ", COMPARISON WITH THE REAL PRODUCTION AND OBSERVED SINERGY EFFECT IN TERMS OF ORGANIC DRY MATTER")
        pos = arange(5)+ .5
        pos2 = arange(5)+.13
        width = 0.75
        plt.ylim([0,dict_substrates[i]+200])
        if dict_real_production[i] > seventyfive_sludge:
            pos2= arange(5)+.03
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), width, color="yellow", label = "Real production")
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), width,color="orange", align = "center", label="Theoretical production")
        else:
            bar(pos,(0, seventyfive_sludge, fifty_sludge,twentyfive_sludge,0), width,color="orange", align = "center", label="Theoretical production")
            bar(pos2,(raw_sludge, dict_real_production[i],0, 0, dict_substrates[i]), width,color="yellow", label = "Real production")
        
        xticks(pos, ("100%-0%", "75%-25%", "50%-50%", "25%-75%" , "0%-100%" ))
        xlabel("Amount of sewage sludge in the mixture % - Amount of "+i+" in the mixture %")
        ylabel("Organic dry matter methane production [m3/t f.m.]")
        title(" SEWAGE SLUDGE MIXED WITH " + i.upper() + ", ORGANIC DRY MATTER")
        if dict_real_production[i] > seventyfive_sludge:
            plt.text(.95, dict_real_production[i] + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        else:
            plt.text(.95, seventyfive_sludge + 10, 'Sinergy:' + str(round(sinergy,2)) + "%")
        grid(True)
        plt.legend()
        
        show()        


if __name__=="__main__":
    theoretical_thermo_biogas_substrates_heat_pretreatment_FM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_thermo_biogas_substrates_heat_pretreatment_ODM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_thermo_methane_substrates_heat_pretreatment_FM(raw_sludge, dict_substrates, dict_real_production)
    theoretical_thermo_methane_substrates_heat_pretreatment_ODM(raw_sludge, dict_substrates, dict_real_production)