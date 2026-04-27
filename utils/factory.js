exports.getAll = (Model) => async (req, res) => {
    try {
        const docs = await Model.find();
        res.status(200).json({ success: true, count: docs.length, data: docs });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
};

exports.getOne = (Model) => async (req, res) => {
    try {
        const doc = await Model.findById(req.params.id);
        if (!doc) return res.status(404).json({ success: false, message: 'No encontrado' });
        res.status(200).json({ success: true, data: doc });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
};

exports.createOne = (Model) => async (req, res) => {
    try {
        const doc = await Model.create(req.body);
        res.status(201).json({ success: true, data: doc });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
};

exports.updateOne = (Model) => async (req, res) => {
    try {
        const doc = await Model.findByIdAndUpdate(req.params.id, req.body, {
            new: true,
            runValidators: true
        });
        if (!doc) return res.status(404).json({ success: false, message: 'No encontrado' });
        res.status(200).json({ success: true, data: doc });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
};

exports.deleteOne = (Model) => async (req, res) => {
    try {
        const doc = await Model.findByIdAndDelete(req.params.id);
        if (!doc) return res.status(404).json({ success: false, message: 'No encontrado' });
        res.status(200).json({ success: true, data: {} });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
};
