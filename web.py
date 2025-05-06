import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



todos = functions.get_todos()

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("this app is used for productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="hidden", label_visibility="hidden", placeholder="Add a To-Do...😎",
              on_change=add_todo, key='new_todo')

print("Hello")

st.session_state