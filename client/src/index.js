import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { RootRouter } from './routers/RootRouter';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import { store } from './common/redux/store';
import { AppThemeProvider } from './modules/app/containers/AppThemeProvider/AppThemeProvider';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
        <AppThemeProvider>
            <React.StrictMode>
                <RootRouter />
            </React.StrictMode>
        </AppThemeProvider>
    </Provider>
);

reportWebVitals();
