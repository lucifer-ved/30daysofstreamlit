import React from "react"
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"

const MyComponent = ({ args }) => {
  const message = args["message"] || "Hello, Streamlit!"

  return (
    <div>
      <p>{message}</p>
    </div>
  )
}

export default withStreamlitConnection(MyComponent)
