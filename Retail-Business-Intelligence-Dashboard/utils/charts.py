import plotly.express as px


def revenue_by_category(sales, categories):
    df = (
        sales.groupby("category_id")["total_cart_price"]
        .sum()
        .reset_index()
    )

    df = df.merge(categories, on="category_id")

    fig = px.bar(
        df,
        x="category_name",
        y="total_cart_price",
        color="category_name",
        text_auto=".2s",
        title="Revenue by Category"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title_x=0.5
    )

    return fig


def top_products(sales, products):
    df = (
        sales.groupby("product_id")["product_total_price"]
        .sum()
        .reset_index()
    )

    df = df.merge(products, on="product_id")

    df = df.sort_values(
        "product_total_price",
        ascending=False
    ).head(10)

    fig = px.bar(
        df,
        x="product_total_price",
        y="product_name",
        orientation="h",
        color="product_total_price",
        title="Top 10 Products"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title_x=0.5
    )

    return fig