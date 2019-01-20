import axelrod as axl


teachers_list = [axl.Defector(), axl.Cooperator(), axl.TitForTat(), axl.TitFor2Tats(), axl.SuspiciousTitForTat()]
print(teachers_list)
tournament = axl.Tournament(teachers_list, turns=2, repetitions=1)
results = tournament.play()

print(results)
# print(results.ranked_names)
print(results.state_distribution)
print(results.normalised_cooperation)
# plot = axl.Plot(results)
# p = plot.boxplot()
# p.show()
