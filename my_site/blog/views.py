from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Mit Desai",
        "date": date(2022, 2, 8),
        "title": "Mountain Hiking",
        "excerpt": """Best Hikin Views.!! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae eos incidunt ipsum, fugiat dolore voluptas itaque vitae est minus nostrum aperiam, obcaecati cum necessitatibus nisi ratione? Itaque esse expedita vero?""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae dignissimos, eveniet qui, sit vel deleniti laudantium impedit totam accusantium minus distinctio nemo numquam perferendis nisi in commodi officiis aut tempore!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea perferendis ducimus iusto, id numquam eveniet corrupti quasi quas, cupiditate suscipit placeat voluptates eum quibusdam, blanditiis delectus a iure ipsam hic.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat perspiciatis autem corrupti esse, hic a eaque sequi officia fugit iste consequatur accusantium natus dolore, nostrum eligendi dolorem officiis perferendis eos.
        """,
    },
    {
        "slug": "chill-in-the-mountains",
        "image": "woods.jpg",
        "author": "Mit Desai",
        "date": date(2022, 2, 9),
        "title": "In to the Woods",
        "excerpt": """Best Chillin Vibes.!! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae eos incidunt ipsum, fugiat dolore voluptas itaque vitae est minus nostrum aperiam, obcaecati cum necessitatibus nisi ratione? Itaque esse expedita vero?""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae dignissimos, eveniet qui, sit vel deleniti laudantium impedit totam accusantium minus distinctio nemo numquam perferendis nisi in commodi officiis aut tempore!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea perferendis ducimus iusto, id numquam eveniet corrupti quasi quas, cupiditate suscipit placeat voluptates eum quibusdam, blanditiis delectus a iure ipsam hic.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat perspiciatis autem corrupti esse, hic a eaque sequi officia fugit iste consequatur accusantium natus dolore, nostrum eligendi dolorem officiis perferendis eos.
        """,
    },
    {
        "slug": "programming-is-great",
        "image": "coding.jpg",
        "author": "Mit Desai",
        "date": date(2022, 2, 10),
        "title": "Programming is Great!!",
        "excerpt": """Coding is a game-changer and the ones who are skilled in coding have a competitive advantage in career. It is true that computer programming was once recognised as a skill reserved for computer nerds and geeks.""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repudiandae dignissimos, eveniet qui, sit vel deleniti laudantium impedit totam accusantium minus distinctio nemo numquam perferendis nisi in commodi officiis aut tempore!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea perferendis ducimus iusto, id numquam eveniet corrupti quasi quas, cupiditate suscipit placeat voluptates eum quibusdam, blanditiis delectus a iure ipsam hic.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat perspiciatis autem corrupti esse, hic a eaque sequi officia fugit iste consequatur accusantium natus dolore, nostrum eligendi dolorem officiis perferendis eos.
        """,
    },
]


def get_date(post):
    return post.get('date')  # or post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',{
        "post":identified_post,
    })
