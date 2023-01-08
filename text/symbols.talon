question [mark]: "?"
(downscore | underscore): "_"
double dash: "--"
# Add symbol at end of line and then insert line below
# From https://github.com/AndreasArvidsson/andreas-talon/blob/master/misc/keys/keys.talon#L28
patch {user.symbol_key}:
        edit.line_end()
    "{symbol_key}"
    edit.line_insert_down()
(bracket | brack | left bracket): "{"
(rbrack | are bracket | right bracket): "}"
triple quote: "'''"
(triple grave | triple back tick | gravy | triple skies):
    insert("```")
(dot dot | dotdot): ".."
pebble: "..."
spam: ", "
plus: "+"
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dubstring:
    '""'
    key(left)
empty escaped (dubstring|dub quotes):
    '\\"\\"'
    key(left)
    key(left)
empty string:
    "''"
    key(left)
empty escaped string:
    "\\'\\'"
    key(left)
    key(left)
(inside parens | args):
	insert("()")
	key(left)   

inside (angle):
	insert("<>")
	key(left)

inside (squares | square brackets | list):
	insert("[]")
	key(left)
inside (bracket | braces):
	insert("{}")
	key(left)
inside percent:
	insert("%%")
	key(left)
inside (quotes | string):
	insert("''")
	key(left)
inside (double quotes | dubquotes):
    user.insert_between('"', '"')
inside (skis | back ticks):
	insert("``")
	key(left)
angle that:
    text = edit.selected_text()
    user.paste("<{text}>")
(square | square bracket) that:
    text = edit.selected_text()
    user.paste("[{text}]")
(bracket | brace) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
(parens | args) that:
    text = edit.selected_text()
    user.paste("({text})")
percent that:
    text = edit.selected_text()
    user.paste("%{text}%")
quote that:
    text = edit.selected_text()
    user.paste("'{text}'")
(double quote | dubquote) that:
    text = edit.selected_text()
    user.paste('"{text}"')
(grave | back tick) that:
    text = edit.selected_text()
    user.paste('`{text}`')
