def get_grade(s1, s2, s3):
    score = (s1+s2+s3)/3
    if 90 <= score and score <= 100:
        return 'A'
    elif 80 <= score and score  < 90:
        return 'B'
    elif 70 <= score and score  < 80:
        return 'C'
    elif 60 <= score and score  < 70:
        return 'D'
    elif 0 <= score and score  < 60:
        return 'F'
        