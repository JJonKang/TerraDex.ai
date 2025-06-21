import React from 'react';

type ButtonProps = {
    label: string;
    onClick: () => void;
};

const Button: React.FC<ButtonProps> = ({
    label,
    onClick
}) => {
    return (
        <button
            onClick = {onClick}
            className = "px-2 py-2 text-purple-600 rounded hover:bg-purple-300"
        >

        {label}
        </button>
    );
};
export {Button};