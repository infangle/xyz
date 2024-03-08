class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leader_at_time = []  
        vote_count = {}  
        leader = None 

        for i, person in enumerate(persons):
            vote_count[person] = vote_count.get(person, 0) + 1
            if leader is None or vote_count[person] >= vote_count[leader]:
                leader = person
            self.leader_at_time.append(leader)


    def q(self, t: int) -> int:

        idx = bisect_right(self.times, t)
        return self.leader_at_time[idx - 1]


        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)