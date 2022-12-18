import git

def read_f(path = "./practice4/gits.txt"):
    with open(path, 'r') as f:
        rows = f.readlines()
    for i in range(len(rows)):
        rows[i] = rows[i].strip()
    return rows

def copy_git(names, path = "./practice4/repos"):
    ls = []

    for i in names:
        repo = i[i.find('/', 13):-4:]
        try:
            git.Repo.clone_from(i, path + repo)
            ls.append(i + ' -- OK')
        except:
            ls.append(i + ' -- FAIL')

    return ls

def write_f(ress, path = "./practice4/res.txt"):
    with open(path, 'w') as f:
        for i in ress:
            f.writelines(i + '\n')

if (__name__ == "__main__"):
    r = read_f()
    l = copy_git(r)
    write_f(l)
    