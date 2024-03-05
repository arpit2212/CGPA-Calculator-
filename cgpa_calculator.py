
question_1 = input("Enter your batch number 1 or 2  : ")

if (question_1 == "2") :

    #take the internal marks of all the subject from user (out of 60)
    Sub_b1_I_1 = float(input("Enter your Maths internal marks (out of 60): "))
    Sub_b1_I_2 = float(input("Enter your Semiconductorinternal marks (out of 60): "))
    Sub_b1_I_3 = float(input("Enter your EEE internal marks (out of 60): "))
    Sub_b1_I_4 = float(input("Enter your PPS internal marks (out of 60): "))
    Sub_b1_I_5 = float(input("Enter your English internal marks (out of 60): "))
    Sub_b1_I_6 = float(input("Enter your Graphic Desgining internal marks (out of 60): "))
    Sub_b1_I_7 = float(input("Enter your Professional skills internal marks (out of 100): "))
    Sub_b1_I_8 = float(input("Enter your Constitution Of India internal marks (out of 100): "))
    Sub_b1_I_9 = float(input("Enter your Enviomental Science internal marks (out of 100): "))

    #calculate percentange of the internal marks of user with 0 credit 

    total_internal_marks_b1_with_0_credit = (Sub_b1_I_1 + Sub_b1_I_2 + Sub_b1_I_3 + Sub_b1_I_4 + Sub_b1_I_5 + Sub_b1_I_6 + Sub_b1_I_7+ Sub_b1_I_8 + Sub_b1_I_9)

    percentage_of_total_internal_marks_b1_with_0_credit = (total_internal_marks_b1_with_0_credit/660)*100

    CGPA_of_total_internal_marks_b1_with_0_credit = ((percentage_of_total_internal_marks_b1_with_0_credit)/9.5)


    #calculate percentange of the internal marks of user without 0 credit

    total_internal_marks_b1_without_0_credit = (Sub_b1_I_1 + Sub_b1_I_2 + Sub_b1_I_3 + Sub_b1_I_4 + Sub_b1_I_5 + Sub_b1_I_6 )

    percentage_of_total_internal_marks_b1_without_0_credit = (total_internal_marks_b1_without_0_credit/360)*100

    CGPA_of_total_internal_marks_b1_without_0_credit = (percentage_of_total_internal_marks_b1_without_0_credit)/9.5

    #print the internal marks with and without 0 credit 

    question_2 = input("if you want to calculate  internal marks then type 1 and if you want to calculate final marks then type 2 : ")

    if (question_2 == "1" ) :


        question_3 = input("You want to see your internal marks with 0 credit then type 1 and if want to calculate without 0 credit then type 2  : ")


        if (question_3 == "1") :
            print("total internal percentage of marks with 0 credit is :",percentage_of_total_internal_marks_b1_with_0_credit)

            print("total internal CGPA of marks with 0 credit is :",CGPA_of_total_internal_marks_b1_with_0_credit)

        elif (question_3 == "2") :
            print("total internal percentage of marks without 0 credit is :",percentage_of_total_internal_marks_b1_without_0_credit)

            print("total internal CGPA of marks without 0 credit is :",CGPA_of_total_internal_marks_b1_without_0_credit)

    elif (question_2 == "2" )  :


        Sub_b1_F_1 = float(input("Enter your Maths expected semster exam mask  (out of 75): "))
        Sub_b1_F_2 = float(input("Enter your Semiconductor expected semster exam mask  (out of 75): "))
        Sub_b1_F_3 = float(input("Enter your EEE  expected semster exam mask  (out of 75): "))
        Sub_b1_F_4 = float(input("Enter your PPS expected semster exam mask  (out of 75): "))
        Sub_b1_F_5 = float(input("Enter your English  expected semster exam mask  (out of 75): "))
        Sub_b1_F_6 = float(input("Enter your Graphic Desginingexpected semster exam mask  (out of 40): "))

        #convert sem marks into 40 and take the percentage

        b1_marks_out_of_40_of_subeject_1 = (Sub_b1_F_1/75)*40
        b1_marks_out_of_40_of_subeject_2 = (Sub_b1_F_2/75)*40
        b1_marks_out_of_40_of_subeject_3 = (Sub_b1_F_3/75)*40
        b1_marks_out_of_40_of_subeject_4 = (Sub_b1_F_4/75)*40
        b1_marks_out_of_40_of_subeject_5 = (Sub_b1_F_5/75)*40
        b1_marks_out_of_40_of_subeject_6 = (Sub_b1_F_6/40)*40

        # total marks with 0 credit 

        total_sem_marks_b1 = b1_marks_out_of_40_of_subeject_2 + b1_marks_out_of_40_of_subeject_3 +b1_marks_out_of_40_of_subeject_4 + b1_marks_out_of_40_of_subeject_5 + b1_marks_out_of_40_of_subeject_6

        total_final_marks_b1_with_0_credit = ( total_internal_marks_b1_with_0_credit + total_sem_marks_b1 )

        percentage_of_total_final_marks_b1_with_0_credit = (total_final_marks_b1_with_0_credit/900)*100

        CGPA_of_total_final_marks_b1_with_0_credit = ((percentage_of_total_final_marks_b1_with_0_credit)/9.5)

        #total marks without 0 credit

        total_final_marks_b1_without_0_credit = (total_internal_marks_b1_without_0_credit + total_sem_marks_b1)

        percentage_of_total_final_marks_b1_without_0_credit = (total_final_marks_b1_without_0_credit/600)*100

        CGPA_of_total_final_marks_b1_without_0_credit = (percentage_of_total_final_marks_b1_without_0_credit)/9.5

        question_5 = input("You want to see your final marks with 0 credit then type 1 and if you want to calculate witout credit then type 2 : ")

        if (question_5 == "1") :
            print("total final percentage of marks with 0 credit is :",percentage_of_total_final_marks_b1_with_0_credit)

            print("total final CGPA of marks with 0 credit is :",CGPA_of_total_final_marks_b1_with_0_credit)

        elif (question_5 == "2") :
            print("total final percentage of marks without 0 credit is :",percentage_of_total_final_marks_b1_without_0_credit)

            print("t1tal fianl CGPA of marks without 0 credit is :",CGPA_of_total_final_marks_b1_without_0_credit)

elif (question_1 == "1") :

    #take the internal marks of all the subject from user (out of 60)
    Sub_b2_I_1 = float(input("Enter your Maths internal marks (out of 60): "))
    Sub_b2_I_2 = float(input("Enter your Chemistry internal marks (out of 60): "))
    Sub_b2_I_3 = float(input("Enter your Bio internal marks (out of 60): "))
    Sub_b2_I_4 = float(input("Enter your PPS internal marks (out of 60): "))
    Sub_b2_I_5 = float(input("Enter your Foriegn Language internal marks (out of 60): "))
    Sub_b2_I_6 = float(input("Enter your Mechanical internal marks (out of 60): "))
    Sub_b2_I_7 = float(input("Enter your Professional skills internal marks (out of 100): "))
    Sub_b2_I_8 = float(input("Enter your nss internal marks (out of 100): "))
    Sub_b2_I_9 = float(input("Enter your poe internal marks (out of 60): "))
    
    #calculate percentange of the internal marks of user with 0 credit 

    total_internal_marks_b2_with_0_credit = (Sub_b2_I_1 + Sub_b2_I_2 + Sub_b2_I_3 + Sub_b2_I_4 + Sub_b2_I_5 + Sub_b2_I_6 + Sub_b2_I_7+ Sub_b2_I_8 + Sub_b2_I_9)

    percentage_of_total_internal_marks_b2_with_0_credit = (total_internal_marks_b2_with_0_credit/620)*100

    CGPA_of_total_internal_marks_b2_with_0_credit = ((percentage_of_total_internal_marks_b2_with_0_credit)/9.5)

    #calculate percentange of the internal marks of user without 0 credit

    total_internal_marks_b2_without_0_credit = (Sub_b2_I_1 + Sub_b2_I_2 + Sub_b2_I_3 + Sub_b2_I_4 + Sub_b2_I_5 + Sub_b2_I_6 + Sub_b2_I_9)

    percentage_of_total_internal_marks_b2_without_0_credit = (total_internal_marks_b2_without_0_credit/420)*100

    CGPA_of_total_internal_marks_b2_without_0_credit = (percentage_of_total_internal_marks_b2_without_0_credit)/9.5

    #print the internal marks with and without 0 credit 

    question_6 = input("you want to calculate internal marks then type 1 and if you want to calculate final marks then type 2: ")

    if (question_6 == "1" ) :


        question_7 = input("You want to see your internal marks with 0 credit then type Y and if you want to calculate without o credit type 2 : ")


        if (question_7 == "1") :
            print("total internal percentage of marks with 0 credit is :",percentage_of_total_internal_marks_b2_with_0_credit)

            print("total internal CGPA of marks with 0 credit is :",CGPA_of_total_internal_marks_b2_with_0_credit)

        elif (question_7 == "2"):
            print("total internal percentage of marks without 0 credit is :",percentage_of_total_internal_marks_b2_without_0_credit)

            print("total internal CGPA of marks without 0 credit is :",CGPA_of_total_internal_marks_b2_without_0_credit)

    elif (question_6 == "2" ) :

        Sub_b2_F_1 = float(input("Enter your Maths expected semster exam mask  (out of 75): "))
        Sub_b2_F_2 = float(input("Enter your Chemistry expected semster exam mask  (out of 75): "))
        Sub_b2_F_3 = float(input("Enter your Bio expected semster exam mask  (out of 75): "))
        Sub_b2_F_4 = float(input("Enter your PPS expected semster exam mask  (out of 75): "))
        Sub_b2_F_5 = float(input("Enter your Foriegn Languages expected semster exam mask (out of 75): "))
        Sub_b2_F_6 = float(input("Enter your expected semster exam mask (out of 70): "))
        Sub_b2_F_7 = float(input("Enter your poe Mechanical expected semster exam mask (out of 40): "))
        
        #convert sem marks into 40 and take the percentage

        b2_marks_out_of_40_of_subeject_1 = (Sub_b2_F_1/75)*40
        b2_marks_out_of_40_of_subeject_2 = (Sub_b2_F_2/75)*40
        b2_marks_out_of_40_of_subeject_3 = (Sub_b2_F_3/75)*40
        b2_marks_out_of_40_of_subeject_4 = (Sub_b2_F_4/75)*40
        b2_marks_out_of_40_of_subeject_5 = (Sub_b2_F_5/75)*40
        b2_marks_out_of_40_of_subeject_6 = (Sub_b2_F_6/75)*40
        b2_marks_out_of_40_of_subeject_7 = (Sub_b2_F_7/40)*40

        # total marks with 0 credit 

        total_sem_marks_b2 = b2_marks_out_of_40_of_subeject_2 + b2_marks_out_of_40_of_subeject_3 +b2_marks_out_of_40_of_subeject_4 + b2_marks_out_of_40_of_subeject_5 + b2_marks_out_of_40_of_subeject_6+Sub_b2_F_7

        total_final_marks_b2_with_0_credit = ( total_internal_marks_b2_with_0_credit + total_sem_marks_b2 )
        percentage_of_total_final_marks_b2_with_0_credit = (total_final_marks_b2_with_0_credit/900)*100
        CGPA_of_total_final_marks_b2_with_0_credit = ((percentage_of_total_final_marks_b2_with_0_credit)/9.5)

        #total marks without 0 credit

        total_final_marks_b2_without_0_credit = (total_internal_marks_b2_without_0_credit + total_sem_marks_b2)

        percentage_of_total_final_marks_b2_without_0_credit = (total_final_marks_b2_without_0_credit/600)*100

        CGPA_of_total_final_marks_b2_without_0_credit = (percentage_of_total_final_marks_b2_without_0_credit)/9.5

        question_8 = input("You want to see your final marks with 0 credit then type 1 and if you want to calculate wiithout 0 credit then type 2  : ")

        if (question_8 == "1") :
            print("total final percentage of marks with 0 credit is :",percentage_of_total_final_marks_b2_with_0_credit)

            print("total final CGPA of marks with 0 credit is :",CGPA_of_total_final_marks_b2_with_0_credit)

        elif (question_8 == "2") :
            print("total final percentage of marks without 0 credit is :",percentage_of_total_final_marks_b2_without_0_credit)

            print("total fianl CGPA of marks without 0 credit is :",CGPA_of_total_final_marks_b2_without_0_credit)
