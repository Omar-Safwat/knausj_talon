# XXX - would be nice to be able pipe these through formatters

from talon import Context, Module

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")

abbreviations = {
    "address": "addr",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "alternative": "alt",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "assembly": "asm",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "auth",
    "away from keyboard": "afk",
    "binary": "bin",
    "boolean": "bool",
    "british columbia": "bc",
    "button": "btn",
    "canada": "ca",
    "centimeter": "cm",
    "char": "chr",
    "character": "char",
    "class": "cls",
    "client": "clt",
    "column": "col",
    "command": "cmd",
    "commandline": "cli",
    "comment": "cmt",
    "compare": "cmp",
    "conference": "conf",
    "config": "cfg",
    "configuration": "cfg",
    "constant": "const",
    "context": "ctx",
    "control": "ctrl",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "database": "db",
    "debug": "dbg",
    "declaration": "decl",
    "declare": "decl",
    "decode": "dec",
    "decrement": "dec",
    "define": "def",
    "definition": "def",
    "description": "desc",
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directory": "dir",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "double": "dbl",
    "dupe": "dup",
    "duplicate": "dup",
    "dynamic": "dyn",
    "encode": "enc",
    "entry": "ent",
    "enumerate": "enum",
    "environment": "env",
    "escape": "esc",
    "etcetera": "etc",
    "example": "ex",
    "exception": "exc",
    "execute": "exec",
    "expression": "exp",
    "extend": "ext",
    "extension": "ext",
    "file system": "fs",
    "framework": "fw",
    "function": "func",
    "funny": "lol",
    "generate": "gen",
    "generic": "gen",
    "history": "hist",
    "hypertext": "http",
    "image": "img",
    "import address table": "iat",
    "import table": "iat",
    "in real life": "irl",
    "increment": "inc",
    "index": "idx",
    "information": "info",
    "initialize": "init",
    "initializer": "init",
    "instance": "inst",
    "integer": "int",
    "interrupt": "int",
    "iterate": "iter",
    "jason": "json",
    "java archive": "jar",
    "javascript": "js",
    "jump": "jmp",
    "keyboard": "kbd",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "language": "lng",
    "length": "len",
    "library": "lib",
    "manitoba": "mb",
    "markdown": "md",
    "message": "msg",
    "meta sploit framework": "msf",
    "meta sploit": "msf",
    "microphone": "mic",
    "milligram": "mg",
    "millisecond": "ms",
    "miscellaneous": "misc",
    "module": "mod",
    "mount": "mnt",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "nb",
    "nova scotia": "ns",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "ontario": "on",
    "operating system": "os",
    "option": "opt",
    "original": "orig",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pico second": "ps",
    "pixel": "px",
    "point": "pt",
    "pointer": "ptr",
    "position independent code": "pic",
    "position independent executable": "pie",
    "position": "pos",
    "previous": "prev",
    "property": "prop",
    "public": "pub",
    "python": "py",
    "quebec": "qc",
    "query string": "qs",
    "random": "rnd",
    "receipt": "rcpt",
    "reference": "ref",
    "references": "refs",
    "register": "reg",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "repel": "repl",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "return": "ret",
    "revision": "rev",
    "ruby": "rb",
    "rust": "rs",
    "saskatchewan": "sk",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "source": "src",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "string": "str",
    "structure": "struct",
    "synchronize": "sync",
    "synchronous": "sync",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "technology": "tech",
    "temp": "tmp",
    "temperature": "temp",
    "temporary": "tmp",
    "text": "txt",
    "time of check time of use": "toctou",
    "token": "tok",
    "ultimate": "ulti",
    "unique id": "uuid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    "verify": "vrfy",
    "versus": "vs",
    "visual studio": "msvc",
    "visual": "vis",
    "web": "www",
    "what the fuck": "wtf",
    "window": "win",
}

ctx = Context()
ctx.lists["user.abbreviation"] = abbreviations
