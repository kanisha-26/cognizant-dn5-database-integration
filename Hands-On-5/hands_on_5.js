// Hands-On 5 - MongoDB CRUD Operations and Aggregation
// Database: college_nosql
// Collection: feedback

// Count total documents
db.feedback.countDocuments();

// Find all feedback with rating 5
db.feedback.find({ rating: 5 });

// Find CS101 feedback with challenging tag
db.feedback.find({
course_code: "CS101",
tags: "challenging"
});

// Display selected fields only
db.feedback.find(
{},
{
student_id: 1,
course_code: 1,
rating: 1,
_id: 0
}
);

// Add needs_review field for low ratings
db.feedback.updateMany(
{ rating: { $lt: 3 } },
{ $set: { needs_review: true } }
);

// Add reviewed tag
db.feedback.updateMany(
{ needs_review: true },
{ $push: { tags: "reviewed" } }
);

// Delete old semester feedback
db.feedback.deleteMany({
semester: "2021-EVEN"
});

// Aggregation Pipeline
db.feedback.aggregate([
{
$match: {
semester: "2022-ODD"
}
},
{
$group: {
_id: "$course_code",
avg_rating: { $avg: "$rating" },
total_feedback: { $sum: 1 }
}
},
{
$project: {
_id: 0,
course_code: "$_id",
average_rating: {
$round: ["$avg_rating", 1]
},
total_feedback: 1
}
},
{
$sort: {
average_rating: -1
}
}
]);

// Create index on course_code
db.feedback.createIndex({
course_code: 1
});
