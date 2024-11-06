import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { RootRouter } from './routers/RootRouter';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import { store } from './common/redux/store';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
        <React.StrictMode>
            <RootRouter />
        </React.StrictMode>
    </Provider>
);

reportWebVitals();
