import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("Simplify Your Day, Every Day ")
st.write("Let's get organized!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="hidden", label_visibility="hidden", placeholder="Add a To-Do...😎",
              on_change=add_todo, key='new_todo')


