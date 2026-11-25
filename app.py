import time
import streamlit as st
from feedback import TASKS, check_code

st.set_page_config(page_title="CodeTutor", page_icon="💻", layout="wide")

defaults = {
    "completed": [],
    "history": [],
    "feedback": None,
    "started": time.time(),
    "task": "Functions"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def change_task():
    st.session_state.feedback = None
    st.session_state.started = time.time()


st.title("CodeTutor")
st.write("Interactive Python learning assistant")
st.caption("Research prototype | Rule-based simulation of AI tutoring")

with st.sidebar:
    st.header("Learning controls")
    task = st.selectbox(
        "Choose an exercise",
        list(TASKS),
        key="task",
        on_change=change_task
    )
    mode = st.radio("Feedback detail", ["Concise", "Detailed"])
    st.divider()
    st.subheader("Progress")
    st.progress(len(st.session_state.completed) / len(TASKS))
    st.write(f"{len(st.session_state.completed)} of {len(TASKS)} tasks completed")
    st.metric("Total attempts", len(st.session_state.history))

    if st.button("Reset session"):
        st.session_state.clear()
        st.rerun()

left, right = st.columns(2)

with left:
    st.subheader("Programming exercise")
    st.info(TASKS[task]["question"])

    code = st.text_area(
        "Your Python code",
        value=TASKS[task]["starter"],
        height=240,
        key=f"code_{task}"
    )

    if st.button("Check my code", type="primary"):
        result = check_code(task, code)
        elapsed = round(time.time() - st.session_state.started, 1)

        st.session_state.feedback = {"task": task, "code": code}
        st.session_state.history.append({
            "Task": task,
            "Feedback mode": mode,
            "Matched": result["correct"],
            "Elapsed seconds": elapsed
        })

        if result["correct"] and task not in st.session_state.completed:
            st.session_state.completed.append(task)

        st.rerun()

with right:
    st.subheader("Tutor feedback")

    submitted = st.session_state.feedback

    if submitted and submitted["task"] == task:
        result = check_code(
            task,
            submitted["code"],
            detailed=(mode == "Detailed")
        )

        if result["correct"]:
            st.success("Supported solution matched")
        else:
            st.warning("Review your submission")

        st.markdown("**Issue**")
        st.write(result["issue"])

        if result["evidence"]:
            st.caption("Evidence from your submitted code")
            st.code(result["evidence"], language="python")

        st.markdown("**Suggestion**")
        st.write(result["suggestion"])

        st.markdown("**Next step**")
        st.write(result["next_step"])

        if code != submitted["code"]:
            st.info("Your code has changed. Submit again to update feedback.")
    else:
        st.info("Submit your code to receive feedback.")

st.divider()
st.subheader("Reflection")

effort = st.slider("How much mental effort did this task require?", 1, 7, 4)
st.caption("1 = very low mental effort; 7 = very high mental effort")

preference = st.radio(
    "Preferred feedback style",
    ["Concise", "Detailed", "No preference"],
    horizontal=True
)

if st.button("Save reflection"):
    st.session_state.reflection = {
        "Mental effort": effort,
        "Preference": preference
    }

if "reflection" in st.session_state:
    st.write("Saved session reflection:", st.session_state.reflection)

with st.expander("View attempt history"):
    if st.session_state.history:
        st.dataframe(st.session_state.history, use_container_width=True)
    else:
        st.write("No attempts recorded yet.")

st.caption(
    "Prototype limitations: submitted code is not executed. "
    "Alternative correct solutions may not be recognised. "
    "Session data is temporary. No live language model is connected."
)
