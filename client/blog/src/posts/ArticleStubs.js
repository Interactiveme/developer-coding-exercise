import React, { Component } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default class ArticleStubs extends Component {

    server = process.env.REACT_APP_SERVER_URL;

    state = {
        posts: []
    }

    componentDidMount() {
        debugger
        axios.get(this.server)
            .then(res => {
                const postData = res.data;
                this.setState({ posts: postData.posts });
        })
    }

    postRoute (post) {
        return `post/${post.slug}`;
    }

    render() {
        return (
            this.state.posts.map(
                (_item, _index) => (
                    <article className="blog-post" key={_index}>
                        <h2 className="blog-post-title">{_item.title}</h2>
                        <p><i>{_item.author}</i></p>
                        <span className="blog-post-stub-content" dangerouslySetInnerHTML = {{__html:_item.content}}/>
                        <Link to={this.postRoute(_item)} className="stretched-link">Continue reading</Link>
                    </article>
                )
            )
        )
    }
}