#The regular expression module. Part of the core distribution.
import re
#For the sqrt function. Part of the core distribution.
import math
#So we can sort 1 and 2d dictionaries by value. Part of the core distribution.
from operator import itemgetter

enrolled = {}
numstudents = {}
numincommon = {}
scores = {}
titles = {}

for line in open("courseenrollment.txt", "r"):
    line = line.rstrip('\s\r\n')
    (student, graddate, spec, term, dept, courseno) = line.split('\t')

# create a variable course that consists of the dept. abbreviation followed by a space and course number
    course=dept+' '+courseno
    
  #2d arrays work well in Python, you just need to do a little initializing.
  #Enrolled never increments values in subdict 'student' so we just assign 1.
    if course not in enrolled:
        enrolled[course] = {student: 1}
    if student not in enrolled[course]:
        enrolled[course][student] = 1
  #numstudents on the other hand does increment the value so we init the key
  #and set the value to zero if the key does not currently exist.
    if course not in numstudents:
        numstudents[course] = 0
  #Then we can just increment away, safely.
    numstudents[course] += 1

# this part calculates the cosine similarity (which you may or may not remember
# from 503 last year) between the entrollment in 2 courses
# this uses some 2 dimensional hash stuff that you don't need to
# worry about for now or perhaps ever
for course1 in enrolled:
    for course2 in enrolled:
    #Initialize each value in the 2d dict. Keeps us from getting key errors
    #later, but we will have to add an extra conditional to a later loop to 
    #handle this change. Rack this up to a difference in how perl and Python
    #handle undefined key in associative arrays.
        if course1 not in numincommon:
            numincommon[course1] = {course2: 0}
        if course2 not in numincommon[course1]:
            numincommon[course1][course2] = 0
        for student in enrolled[course2]:
            if student in enrolled[course1]:
        # if the same student is enrolled in both courses
        # increment the counter for students in common
                numincommon[course1][course2] += 1
        denominator = math.sqrt(numstudents[course1] * numstudents[course2])
    #Same initialization as numincommon, same reason.
        if course1 not in scores:
            scores[course1] = {course2: 0}
        if course2 not in scores[course1]:
            scores[course1][course2] = 0
        scores[course1][course2] = numincommon[course1][course2]/denominator
    
for line in open("coursetitles.txt", "r"):
    line = line.rstrip('\s\r\n')
    (course, title) = line.split('\t')

# strip trailing sections "-1" and spaces from the course numbers
# and replace underscores with spaces. assign the result to the variable "course2"
    course=course.replace('-1',"")
    course2 = course.replace("_"," ")

# Regex for sequent if/continue
si_re = re.compile(r"^SI \d+.*")
found_re = re.compile(r"SI 50[01234].*")

# create a new text file called datatest
test = open("pairs.txt",'w')
test.write("Source Course"+"\t"+"Target Course"+"\t"+"Cosine Similarity")
for course1 in sorted(scores):
# skip if course was not sufficiently popular
    if (numstudents[course1] < 5) : continue
# skip if the course is not an SI course (use regexp)
    if (si_re.match(course1) is None): continue
# skip if the course is one of the foundations: 500,501,502,503,504
    if found_re.match(course1): continue

    for course2,score in sorted(scores[course1].items(), 
                                key=itemgetter(1),reverse = True):

# skip if the course (course2) is the one we're asking about (course1)
        if course2 == course1 : continue
# skip if (course2) is one of the old foundations: 501,502,503,504
        if found_re.match(course2) : continue
# only consider course2 if the number of students in common is >=1
        if(numincommon[course1][course2] < 1): continue

        # write the data set to pairs.txt
        test.write("\n%s\t%s\t%s" % (course1,course2,score) )

