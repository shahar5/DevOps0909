properties([pipelineTriggers([githubPush()])])

node {
    stage("clone") {
        git "https://github.com/shahar5/DevOps0909.git"
    }
    stage("show files") {
        bat "dir"
    }
}
