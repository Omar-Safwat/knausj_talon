find it:
    edit.find()

next one:
    edit.find_next()

trip: edit.left()

trip <number_small> times: user.left_n(number_small)

hop: edit.right()

hop <number_small> times: user.right_n(number_small)

drain: edit.word_left()

drain <number_small> times: user.words_left(number_small)
step: edit.word_right()

step <number_small> times: user.words_right(number_small)

up: user.up_n(1)

up <number_small> times: user.up_n(number_small)

down: user.down_n(1)

down <number_small> times: user.down_n(number_small)

tail: edit.line_end()

head: edit.line_start()

go way left:
    edit.line_start()
    edit.line_start()

go way right:
    edit.line_end()

go way down:
    edit.file_end()

go way up:
    edit.file_start()

go bottom:
    edit.file_end()

go top:
    edit.file_start()

go page down:
    edit.page_down()

go page up:
    edit.page_up()

# selecting
select line:
    edit.select_line()

select all:
    edit.select_all()

select left:
    edit.extend_left()

select right:
    edit.extend_right()

select up:
    edit.extend_line_up()

select down:
    edit.extend_line_down()

select word:
    edit.select_word()

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()

select way left:
    edit.extend_line_start()

select way right:
    edit.extend_line_end()

select way up:
    edit.extend_file_start()

select way down:
    edit.extend_file_end()

# editing
(ship | indent [more]):
    edit.indent_more()

(dock | indent less | out dent):
    edit.indent_less()

# deleting
clear line:
    edit.delete_line()

wiper: user.delete_word_left_n(1)

wiper <number_small> times: user.delete_word_left_n(number_small)

swallow: user.delete_word_right_n(1)

swallow <number_small> times: user.delete_word_right_n(number_small)

clear head:
    edit.extend_line_start()
    edit.delete()

clear tail:
    edit.extend_line_end()
    edit.delete()

clear way up:
    edit.extend_file_start()
    edit.delete()

clear way down:
    edit.extend_file_end()
    edit.delete()

clear all:
    edit.select_all()
    edit.delete()

#copy commands
copy all:
    edit.select_all()
    edit.copy()
#to do: do we want these variants, seem to conflict
# copy left:
#      edit.extend_left()
#      edit.copy()
# copy right:
#     edit.extend_right()
#     edit.copy()
# copy up:
#     edit.extend_up()
#     edit.copy()
# copy down:
#     edit.extend_down()
#     edit.copy()

copy word:
    edit.select_word()
    edit.copy()

copy word left:
    edit.extend_word_left()
    edit.copy()

copy word right:
    edit.extend_word_right()
    edit.copy()

copy line:
    edit.select_line()
    edit.copy()

#cut commands
cut all:
    edit.select_all()
    edit.cut()
#to do: do we want these variants
# cut left:
#      edit.select_all()
#      edit.cut()
# cut right:
#      edit.select_all()
#      edit.cut()
# cut up:
#      edit.select_all()
#     edit.cut()
# cut down:
#     edit.select_all()
#     edit.cut()

cut word:
    edit.select_word()
    edit.cut()

cut word left:
    edit.extend_word_left()
    edit.cut()

cut word right:
    edit.extend_word_right()
    edit.cut()

cut line:
    edit.select_line()
    edit.cut()
