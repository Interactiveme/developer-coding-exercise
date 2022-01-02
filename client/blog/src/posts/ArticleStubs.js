import React, { Component } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default class ArticleStubs extends Component {

    state = {
        posts: []
    }

    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/`)
            .then(res => {
                const postData = res.data;
                this.setState({ posts: postData.data });
        })
    }

    postRoute (post) {
        return `post/${post.slug}`;
    }

    render() {
        return (
            this.state.posts.map(
                (_item, _index) => (
                    <article className="blog-post">
                        <h2 className="blog-post-title">{_item.title}</h2>
                        <p>{_item.content}</p>
                        <Link to={this.postRoute(_item)} className="stretched-link">Continue reading</Link>
                    </article>
                )
            )
        )
    }
}