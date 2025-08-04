import streamlit as st
import os
import yaml

PROMPT_DIR = "prompts"

def load_prompts():
    prompts = []
    if not os.path.exists(PROMPT_DIR):
        return prompts
    for folder in os.listdir(PROMPT_DIR):
        prompt_path = os.path.join(PROMPT_DIR, folder)
        if os.path.isdir(prompt_path):
            versions = []
            for file in sorted(os.listdir(prompt_path)):
                if file.endswith(".md"):
                    with open(os.path.join(prompt_path, file), "r", encoding="utf-8") as f:
                        content = f.read()
                    versions.append({
                        "version": file.replace(".md", ""),
                        "content": content
                    })
            prompts.append({"title": folder.replace("_", " ").title(), "versions": versions})
    return prompts

def display_prompt(prompt):
    st.subheader(f"📄 {prompt['title']}")
    for v in prompt['versions']:
        with st.expander(f"🔄 Version: {v['version']}"):
            st.code(v['content'], language="markdown")

st.set_page_config(page_title="PromptMirror", layout="wide")
st.title("🪞 PromptMirror")
st.caption("Track and share your evolving AI prompts")

prompts = load_prompts()
if not prompts:
    st.warning("No prompts found. Add markdown files under `prompts/<prompt_name>/v1.md`.")

for prompt in prompts:
    display_prompt(prompt)

st.markdown("---")
st.markdown("Made for tech creators ✨")
