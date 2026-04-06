# Once upon a time, in a [adjective] [noun],
# there lived a [adjective] [noun].
# Every day, the [noun] would [verb] [adverb].
# One day, a [adjective] [noun] appeared
# and [verb] the [noun] away.
# The [noun] was [adjective] and [emotion].

noun1 = input("place \n->")
ajactive1 = input("adjective for place \n->")
character1 = input("character \n->")
character1_adjactive1 = input("adjective for character \n->")
verb1 = input("verb for action character would do \n->")
adverb1 = input("adverb to modify previous verb \n->")
character2 = input("second character \n->")
character2_adjactive1 = input("adjective for second character \n->")
verb2 = input("verb for action second character takes against first character \n->")
character2_adjactive2 = input("adjective for second character after the fact \n->")
emotion = input("emotion second character feels \n->")

print ("Once upon a time, in a "+ajactive1+" "+noun1+",\n"
       "there lived a "+character1_adjactive1+" "+character1+".\n"
       "Every day, the "+character1+" "+verb1+" "+adverb1+".\n"
       "One day, a "+character2_adjactive1+" "+character2+" appeared,"
       "and "+verb2+" the "+character1+" away.\n"
       "The "+character2+" was "+character2_adjactive2+" and "+emotion+".")