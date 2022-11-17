


def checksubsystemConnectivity(maxTime=60):
    status = 'inprogress'
    totalTime = 0

    while status == 'inprogress' and totalTime < maxTime:
        print('Nitya checking connectivity...')
        status = "completed"
        totalTime +=5




checksubsystemConnectivity(maxTime=60)