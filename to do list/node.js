const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

mongoose.connect('mongodb://localhost:27017/todos', { useNewUrlParser: true, useUnifiedTopology: true });

const todoSchema = new mongoose.Schema({
    text: String,
    completed: Boolean
});

const Todo = mongoose.model('Todo', todoSchema);

// Create a new todo
app.post('/api/todos', async (req, res) => {
    try {
    const todo = new Todo({ text: req.body.text, completed: false });
    const savedTodo = await todo.save();
    res.send(savedTodo);
    } catch (err) {
    res.status(500).send(err);
    }
});

// Get all todos
app.get('/api/todos', async (req, res) => {
    try {
    const todos = await Todo.find();
    res.send(todos);
    } catch (err) {
    res.status(500).send(err);
    }
});

// Update a todo
app.put('/api/todos/:id', async (req, res) => {
    try {
    const updatedTodo = await Todo.findByIdAndUpdate(req.params.id, { $set: { text: req.body.text, completed: req.body.completed } }, { new: true });
    res.send(updatedTodo);
    } catch (err) {
    res.status(500).send(err);
    }
});

// Delete a todo
app.delete('/api/todos/:id', async (req, res) => {
    try {
    const deletedTodo = await Todo.findByIdAndRemove(req.params.id);
    res.send(deletedTodo);
    } catch (err) {
    res.status(500).send(err);
    }
});

app.get('/debug', (req, res) => {
    res.send({
    message: 'This is a test endpoint for debugging purposes only',
    express: express,
    mongoose: mongoose,
    app: app
    });
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});

