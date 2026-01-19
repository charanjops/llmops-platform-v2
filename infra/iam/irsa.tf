resource "aws_iam_role_policy" "bedrock" {
  role = aws_iam_role.eks.name
  policy = jsonencode({
    Version="2012-10-17",
    Statement=[{Effect="Allow",Action=["bedrock:InvokeModel"],Resource="*"}]
  })
}