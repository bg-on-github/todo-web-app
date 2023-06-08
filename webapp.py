import streamlit as st
import functions as f

todos = f.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    f.write_todos(todos)

st.title("My Todo App")
st.subheader("List of todos:")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=' ', placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
