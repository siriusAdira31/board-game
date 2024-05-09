from Deterministic_V_Value.Agent import Agent

if __name__ == "__main__":
    ag = Agent()
    ag.play(500)
    print(ag.show_values())
