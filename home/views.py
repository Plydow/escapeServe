from django.shortcuts import render, HttpResponse, redirect
import string, random, time, json, pprint

global advancement, s_time, timed
advancement = 0

mdp_val = json.load(open('config.json', 'r', encoding='utf8'))
pprint.pprint(mdp_val)


def restart(request):
    global advancement
    advancement = 0
    return redirect('step')

def home(request):
    global advancement, s_time
    if request.GET.get('start'):
        advancement = 1
        s_time = time.time()
        return redirect('step')

    return render(request, 'index.html')

def finish(request):
    global advancement, timed
    timed = int(time.time() - s_time)
    h, m = divmod(timed, 3600)
    m, s = divmod(m, 60)

    m = f"0{m}"[-2:]
    s = f"0{s}"[-2:]

    time_str = f"{h}:{m}:{s}"
    if request.GET.get('finish'):
        advancement = 0
        return redirect('step')

    return render(request, 'finish.html', {'timed':time_str})

def step(request):
    global advancement
    print(f"LOG: LEVEL {advancement}")
    if advancement == 0:
        return home(request)
    else:
        key = str(advancement)
        error_flag = False
        if key in mdp_val:
            work = mdp_val[key]
            if request.method == 'POST':
                if request.POST.get(work['result_var'], None) == work['result']:
                    advancement += 1
                    return redirect('step')
                else:
                    error_flag = True

            work['result_var'] = "".join([random.choice(string.ascii_letters) for _ in range(10)])

            return render(request, 'base.html', work | {'error_flag':error_flag})

        else:
            return finish(request)
