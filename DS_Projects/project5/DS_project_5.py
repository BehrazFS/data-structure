import os
import traceback
from Graph import Graph, Vertex, IntegerGraph
from ArrayList import ArrayList
from HashMap import HashMap
from Classes import User, MD5, MutableBool, Post, HashGraph, SuggestGraph, MergeSort
import re

last_user_code = -1


def get_code():
    global last_user_code
    last_user_code += 1
    return last_user_code


users = Graph()
int_users = IntegerGraph(1)
cities = Graph()
# --------------------
cities.add_vertex("Bandar Anzali")  # 0
cities.add_vertex("Masal")  # 1
cities.add_vertex("Somee Sara")  # 2
cities.add_vertex("Khomam")  # 3
cities.add_vertex("Fuman")  # 4
cities.add_vertex("Rasht")  # 5
cities.add_vertex("Shaft")  # 6
cities.add_vertex("Astaneh")  # 7
cities.add_vertex("Lahijan")  # 8
cities.add_vertex("Rudbar")  # 9
cities.add_vertex("Siahkal")  # 10
cities.add_vertex("Langrud")  # 11
cities.add_edge_two_way(cities.vertices[0], cities.vertices[3], 30)
cities.add_edge_two_way(cities.vertices[0], cities.vertices[2], 60)
cities.add_edge_two_way(cities.vertices[1], cities.vertices[2], 25)
cities.add_edge_two_way(cities.vertices[1], cities.vertices[4], 32)
cities.add_edge_two_way(cities.vertices[2], cities.vertices[4], 13)
cities.add_edge_two_way(cities.vertices[4], cities.vertices[6], 2)
cities.add_edge_two_way(cities.vertices[2], cities.vertices[5], 27)
cities.add_edge_two_way(cities.vertices[3], cities.vertices[5], 18)
cities.add_edge_two_way(cities.vertices[5], cities.vertices[6], 29)
cities.add_edge_two_way(cities.vertices[5], cities.vertices[7], 35)
cities.add_edge_two_way(cities.vertices[6], cities.vertices[9], 75)
cities.add_edge_two_way(cities.vertices[5], cities.vertices[9], 66)
cities.add_edge_two_way(cities.vertices[5], cities.vertices[10], 42)
cities.add_edge_two_way(cities.vertices[5], cities.vertices[8], 45)
cities.add_edge_two_way(cities.vertices[7], cities.vertices[8], 20)
cities.add_edge_two_way(cities.vertices[9], cities.vertices[10], 70)
cities.add_edge_two_way(cities.vertices[10], cities.vertices[8], 16)
cities.add_edge_two_way(cities.vertices[8], cities.vertices[11], 16)
cities.add_edge_two_way(cities.vertices[10], cities.vertices[11], 31)
distances = cities.get_Floyd_warshall()
distances = distances[11]
for d in range(12):
    distances[d][d] = 0
# print(distances)
# --------------------
sort_by = MutableBool()
md5 = MD5()
all_usernames = ArrayList()
all_posts = ArrayList()
post_titles = ArrayList()
sug = SuggestGraph(users)
hashgraph = HashGraph()
valid_commands = [
    re.compile(r"^\s*exit\s*$", re.IGNORECASE),  # 0
    re.compile(r"^\s*sign up (\w+) (\w+)\s*$", re.IGNORECASE),  # 1
    re.compile(r"^\s*sign in (\w+) (\w+)\s*$", re.IGNORECASE),  # 2
    re.compile(r"^\s*sign out\s*$", re.IGNORECASE),  # 3
    re.compile(r"\s*help\s*$", re.IGNORECASE),  # 4
    re.compile(r"\s*cls\s*$", re.IGNORECASE),  # 5
    re.compile(r"^\s*bash (\w+\.txt)\s*$", re.IGNORECASE),  # 6 bash
    re.compile(r"^\s*profile (\w+)\s*$", re.IGNORECASE),  # 7
    re.compile(r"^\s*follow (\w+)\s*$", re.IGNORECASE),  # 8
    re.compile(r"^\s*unfollow (\w+)\s*$", re.IGNORECASE),  # 9
    re.compile(r"^\s*post (\w+)\s*$", re.IGNORECASE),  # 10
    re.compile(r"^\s*hfollow (\w+)\s*$", re.IGNORECASE),  # 11
    re.compile(r"^\s*hunfollow (\w+)\s*$", re.IGNORECASE),  # 12
    re.compile(r"^\s*notif\s*$", re.IGNORECASE),  # 13
    re.compile(r"^\s*feed (ts|tn|as|an)\s*$", re.IGNORECASE),  # 14
    re.compile(r"^\s*like (\w+)\s*$", re.IGNORECASE),  # 15
    re.compile(r"^\s*suggest\s*$", re.IGNORECASE),  # 16
    re.compile(r"^\s*dsuggest\s*$", re.IGNORECASE),  # 17
    re.compile(r"^\s*popular\s*$", re.IGNORECASE),  # 18
    re.compile(r"^\s*activity (\w+)\s*$", re.IGNORECASE),  # 19
    re.compile(r"^\s*hsearch (\w+)\s*$", re.IGNORECASE),  # 20
    re.compile(r"^\s*explore\s*$", re.IGNORECASE),  # 21
    re.compile(r"^\s*scc\s*$", re.IGNORECASE),  # 22
]
current_user: User = None
exited = False
count = 0
admin = User("admin", md5.md5hash("admin"), get_code())
bio = "im admin"
city = "Rasht"
admin.city = cities.get(city)
all_usernames.add(admin.username)
users.add_vertex(admin)
sug.add_user(admin)
while not exited:
    try:
        full_name = (current_user.username if current_user is not None else "null")
        if count == 0:
            command = input(fr"Home page :{full_name} -> ")
        else:
            command = lines[len(lines) - count]
            print(fr"Home page :{full_name} -> " + command)
            count -= 1
        # exit:
        match = re.match(valid_commands[0], command)
        if match:
            exited = True
        # cls:
        match = re.match(valid_commands[5], command)
        if match:
            os.system("cls")
        # help
        match = re.match(valid_commands[4], command)
        if match:
            help_ = r"""    valid commands:
        [00] exit -> to exit
        [01] help -> to show help
        [02] sign up 'username' 'password' -> to sign up
        [03] sign in 'username' 'password' -> to sign in
        [04] sign out -> to sign out
        [05] cls -> to clear console
        [06]  bash 'file_name.txt' -> to run commands from a bash file
        .
        .
        ."""
            print(help_)
        # sign up:
        match = re.match(valid_commands[1], command)
        if match:
            if current_user is None:
                new_user = User(match.groups()[0], md5.md5hash(match.groups()[1]), get_code())
                if new_user.username in all_usernames:
                    print("duplicate username")
                else:
                    if count == 0:
                        bio = input("enter your bio : ")
                        city = input("enter your city : ")
                    else:
                        print("enter your bio : ", lines[len(lines) - count])
                        bio = lines[len(lines) - count]
                        count -= 1
                        print("enter your city : ", lines[len(lines) - count])
                        city = lines[len(lines) - count]
                        count -= 1
                    new_user.bio = bio
                    if cities.get(city) is None:
                        print("invalid city name")
                    else:
                        new_user.city = cities.get(city)
                        all_usernames.add(new_user.username)
                        users.add_vertex(new_user)
                        int_users.addVertex(1)
                        sug.add_user(new_user)
                        print("signed up successfully")

        # sign in:
        match = re.match(valid_commands[2], command)
        if match:
            if current_user is None:
                user = User(match.groups()[0], md5.md5hash(match.groups()[1]), -1)
                if users.get(user) is not None and users.get(user).data.password == user.password:
                    current_user = users.get(user).data
                    # print(current_user)
                    print("signed in successfully")
                else:
                    print("invalid username or password")
        # sign out:
        match = re.match(valid_commands[3], command)
        if match:
            current_user = None
            print("signed out successfully")

        #  bash bash_name.txt:
        match = re.match(valid_commands[6], command)
        if match:
            file_name = match.groups()[0]
            with open(file_name, "r") as bash_file:
                lines = bash_file.readlines()
                for kk in range(len(lines)):
                    if lines[kk][-1] == '\n':
                        lines[kk] = lines[kk][:-1]
                count = len(lines)
                print("bash loaded")
        # profile ...
        match = re.match(valid_commands[7], command)
        if match:
            if current_user is not None:
                user: User = User(match.groups()[0], md5.md5hash("null"), -1)
                user: Vertex = users.get(user)
                if user is None:
                    print("user not found")
                else:
                    user: User = user.data
                    print("username : ", user.username)
                    print("bio : ", user.bio)
                    print("city : ", user.city)
                    print(f"followers : {user.get_followers(users).filled} : ", user.get_followers(users))
                    print(f"following : {user.get_following(users).filled} : ", user.get_following(users))
                    print("posts : ", user.posts)
                    # for test:
                    # print(user.hash_follow)
                    # print(user.activity)
                    # print(user.feed)
                    # print(user.notifications)
        # follow ...
        match = re.match(valid_commands[8], command)
        if match:
            if current_user is not None:
                user = User(match.groups()[0], md5.md5hash("null"), -1)
                user: Vertex = users.get(user)
                if user is None:
                    print("user not found")
                else:
                    users.add_edge(users.get(current_user), user)
                    int_users.addEdge(users.get(current_user).index, user.index)
                    current_user.activity.add(f"follow {user.data.username}")
                    sug.follow(users.get(current_user), user, current_user.get_vfollowers(users),
                               user.data.get_vfollowing(users))

        # unfollow ...
        match = re.match(valid_commands[9], command)
        if match:
            if current_user is not None:
                user = User(match.groups()[0], md5.md5hash("null"), -1)
                user: Vertex = users.get(user)
                if user is None:
                    print("user not found")
                else:
                    users.remove_edge(users.get(current_user), user)
                    int_users.removeEdge(users.get(current_user).index, user.index)
                    current_user.activity.add(f"unfollow {user.data.username}")
                    sug.unfollow(users.get(current_user), user, current_user.get_vfollowers(users),
                                 user.data.get_vfollowing(users))
        # post ...
        match = re.match(valid_commands[10], command)
        if match:
            if current_user is not None:
                title = match.groups()[0]
                if title in post_titles:
                    print("duplicate title")
                else:
                    if count == 0:
                        text = input("enter text: ")
                        hashes = input("hashtags: ").split(",")
                    else:
                        print("enter text: ", lines[len(lines) - count])
                        text = lines[len(lines) - count]
                        count -= 1
                        print("hashtags: ", lines[len(lines) - count])
                        hashes = lines[len(lines) - count].split(",")
                        count -= 1
                    p = Post(writer=current_user, title=title, text=text)
                    hashgraph.add_vertex(p, kind="post")
                    v1 = hashgraph.get_post(p)
                    for h in hashes:
                        if hashgraph.get(h) is None:
                            hashgraph.add_vertex(h, kind="hash")
                        v2 = hashgraph.get_hash(h)
                        hashgraph.add_edge_two_way(v1, v2)
                    current_user.posts.add(p)
                    all_posts.add(p)
                    post_titles.add(p.title)
                    for a in current_user.get_followers(users):
                        a.notifications.add(f"{current_user.username} shared a new post title:{p.title}")
                        a.feed.add(p)
                    current_user.activity.add(f"shared post title:{p.title}")

        # hfollow ...
        match = re.match(valid_commands[11], command)
        if match:
            if current_user is not None:
                current_user.hash_follow.add(match.groups()[0])
                current_user.activity.add(f"follow {match.groups()[0]}")

        # hunfollow ...
        match = re.match(valid_commands[12], command)
        if match:
            if current_user is not None:
                current_user.hash_follow.remove(match.groups()[0])
                current_user.activity.add(f"unfollow {match.groups()[0]}")
        # notif
        match = re.match(valid_commands[13], command)
        if match:
            if current_user is not None:
                current_user.notifications.reverse()
                for i in current_user.notifications:
                    print(i)
                current_user.notifications = ArrayList()
        # feed ts|tn|as|an
        match = re.match(valid_commands[14], command)
        if match:
            if current_user is not None:
                sorting = match.groups()[0]
                temp = ArrayList()
                for i in current_user.feed:
                    temp.add(i)
                if sorting == "tn":
                    pass
                elif sorting == "ts":
                    temp.reverse()
                elif sorting == "as":
                    temp.sort()
                elif sorting == "an":
                    temp.sort()
                    temp.reverse()
                ll = 0
                for j in temp:
                    print(ll, " : ", j)
                    ll += 1
        # like ...
        match = re.match(valid_commands[15], command)
        if match:
            if current_user is not None:
                for i in all_posts:
                    # i = Post()
                    if i.title == match.groups()[0]:
                        i.likes += 1
                        i.writer.popularity += 1
                        i.likers.add(current_user)
                        i.writer.notifications.add(f"{current_user.username} liked your post title:{i.title}")
                        current_user.activity.add(f"liked {i.writer.username} post title:{i.title}")
        # suggest
        match = re.match(valid_commands[16], command)
        if match:
            if current_user is not None:
                for i in sug.get_suggest(current_user):
                    if i[0].data not in current_user.get_following(users) and i[0].data != current_user:
                        print(i[0].data)
                # print(current_user.get_followers(users))
                # print(sug.adjacency_matrix)
                # print(sug.adjacency_list)
                # print(sug.edges)
                # print(sug.vertices)
                # sug = SuggestGraph(users)
                # print(sug.adjacency_matrix)
                # print(sug.adjacency_list)
                # print(sug.edges)
                # print(sug.vertices)
        # dsuggest
        match = re.match(valid_commands[17], command)
        if match:
            if current_user is not None:
                temp = ArrayList()
                for i in users.vertices:
                    if i.data != current_user:
                        temp.add([i, distances[i.data.city.index][current_user.city.index]])


                def compare(a, b):
                    if a[1] <= b[1]:
                        return True
                    return False


                sort = MergeSort(compare)
                sort.sort(temp)
                for i in temp:
                    print(i[1], " : ", i[0].data)
        # admin: populars
        match = re.match(valid_commands[18], command)
        if match:
            if current_user is not None and current_user.username == "admin":
                temp = ArrayList()
                for i in users.vertices:
                    temp.add([i, i.data.popularity])


                def compare(a, b):
                    if a[1] >= b[1]:
                        return True
                    return False


                sort = MergeSort(compare)
                sort.sort(temp)
                for i in temp:
                    print(i[1], " : ", i[0].data)
        # admin: activity
        match = re.match(valid_commands[19], command)
        if match:
            if current_user is not None and current_user.username == "admin":
                user: User = User(match.groups()[0], md5.md5hash("null"), -1)
                user: Vertex = users.get(user)
                if user is None:
                    print("user not found")
                else:
                    user: User = user.data
                    temp = ArrayList()
                    for i in user.activity:
                        temp.add(i)
                    temp.reverse()
                    for i in temp:
                        print(i)
        # admin: scc
        match = re.match(valid_commands[22], command)
        if match:
            if current_user is not None and current_user.username == "admin":
                int_users.SCC(users)
        # hsearch
        match = re.match(valid_commands[20], command)
        if match:
            if current_user is not None:
                hash: str = match.groups()[0]
                hash: Vertex = hashgraph.get_hash(hash)

                if hash is None:
                    print("hash not found")
                else:
                    for i in hashgraph.adjacency_list[hash.index]:
                        print(i[0].data)
        # explore
        match = re.match(valid_commands[21], command)
        if match:
            if current_user is not None:
                arr = ArrayList()
                for post in all_posts:
                    val = 0
                    v: Vertex = hashgraph.get_post(post)
                    hashes = hashgraph.get_hashes_by_post(post)
                    for h in hashes:
                        if h in current_user.hash_follow:
                            val += 1
                    arr.add([v, val])


                def compare(a, b):
                    if a[1] >= b[1]:
                        return True
                    return False


                sort = MergeSort(compare)
                sort.sort(arr)
                for i in arr:
                    print(i[1], " : ", i[0].data)
    except Exception as ex:
        print("an unknown error has occurred")
        print("more info : ", ex)
        print(traceback.format_exc())
