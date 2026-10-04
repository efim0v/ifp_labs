# ifp_labs

University Python labs from December 2022: three small command-line exercises
and a throwaway Django site.

This repository has no practical value. The Django part is a test site built
to poke at the framework by hand and see how models, views and templates fit
together — nothing more. It stays public as a keepsake from the time when code
was still written by hand, one line after another.

## What is inside

| Path | What it is |
|---|---|
| [`lab_1.py`](lab_1.py) | Prints Pascal's triangle with the given number of rows |
| [`lab_2.py`](lab_2.py) | Checks whether a sequence of `()`, `[]`, `{}` brackets is balanced |
| [`lab_3/`](lab_3) | Caesar cipher for Russian and English text, file to file |
| [`django_crud/`](django_crud) | Django site with create / read / update / delete pages for universities and their students |

The Django project started from the public
[rayed/django_crud](https://github.com/rayed/django_crud) example and was
reworked around a `university_fbv` app with two models, `University` and
`Student`, built on function-based views. One of the example's book apps,
`books_fbv_user`, is still in the tree but no longer routed.
`django_crud/README.md` is the original example's README and still describes
its book apps.

## Running

The command-line labs need only Python 3:

```sh
python lab_1.py 5
python lab_2.py "{[()]}"
python lab_3/main.py -l EN -O 3 -i lab_3/input.txt -o lab_3/output.txt
```

The Django site:

```sh
cd django_crud
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd apps
python manage.py migrate
python manage.py runserver
```

Then open <http://localhost:8000/>.
