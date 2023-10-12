# Learning From Free-Text Human Feedback – Collect New Datasets Or Extend Existing Ones?
To support research into methods for learning from free-text human feedback, feedback detection, or feedback annotation, we publish the EURTAD dataset. It consists of 1,155 dialogs from various domains. In order to maintain reusability, we provide the dialogs in a unified json format that extends the original annotations with error and user response type annotations. The following listing shows the dialog structure:

\begin{lstlisting}[linewidth=\columnwidth,breaklines=true,showstringspaces=false,language=Python]
{
    "unique_id": "unique id in the context of EURTAD, e.g., PMUL0121.json_multiwoz_train",
    "id": "dataset-specific id, e.g., PMUL0121.json",
    "turns": [
        {
            "utterance": {
                "text": "text of the utterance",
                "original_annotations": [
                    ...
                ],
                "error_type": "the error type, e.g., E5",
                "error_type_comment": "the annotators comment for why this is an error"
            },
            "response": {
                "text": "text of the response",
                "original_annotations": [
                    ...
                ],
                "response_type": "The user response type, e.g., UR5"
            }
        },
        ...
    ]
}

\end{lstlisting}
