# Independent audit: a near-width word for two central layers

## Verdict

The proposed construction is correct, after making one harmless convention
explicit: when the two distinguished coordinates are not both positive, a
middle-layer point with at least two positive coordinates is assigned **any
fixed pair** of its positive coordinates.  Points with only one positive
coordinate cannot be handled by a two-lower-cover edge and, in the unequal
box version, are appended literally.  They do not occur in the balanced
four-box case.

For the balanced box

\[
    P_m=[0,m]^4,
\]

there is a word of length

\[
    |(P_m)_{2m}|+O(m^2)
\]

whose singleton values contain every point of rank \(2m-1\), and whose
adjacent coordinatewise maxima contain every point of rank \(2m\).  One
fully explicit (deliberately crude) bound is

\[
    |(P_m)_{2m}|+\frac{47}{2}m^2+\frac{25}{2}m.
\]

The proof extends uniformly to every fixed-dimensional unequal box.  If
\(P=\prod_{i=1}^D[0,\ell_i]\), \(S=\sum_i\ell_i\), and
\(r=\lfloor S/2\rfloor\), then, provided at least two coordinates have
positive capacity, there is a word of length

\[
    |P_r|+O_D(S^{D-2})
\]

covering every point of \(P_{r-1}\) as a singleton and every point of
\(P_r\) as either an adjacent maximum or one of at most \(D\) literal
entries.  Since products of chains are rank-unimodal, \(|P_r|=w(P)\).

This is a genuine positive local theorem.  It does **not** yet cover the
other ranks of the box, so by itself it is not the missing construction for
the full max-word problem.

## 1. Balanced four-box construction

Let

\[
    V=\{v\in[0,m]^4:\ |v|=2m-1\},\qquad
    Z=\{z\in[0,m]^4:\ |z|=2m\}.
\]

Assume \(m\ge1\).  Every \(z\in Z\) has at least two positive coordinates:
a point supported on one coordinate has rank at most \(m<2m\).

For every \(z\in Z\), choose an unordered pair \(p(z)=\{i,j\}\) of positive
coordinates by the rule

\[
 p(z)=\{1,2\}\quad\hbox{if }z_1,z_2>0,
\]

and otherwise choose any predetermined pair of positive coordinates.  Form
the graph \(G\) with vertex set \(V\) and one edge

\[
    e_z=\{z-e_i,z-e_j\}
\]

for each \(z\in Z\).  The endpoints are distinct lower-layer points, and

\[
    (z-e_i)\vee(z-e_j)=z,                         \tag{1}
\]

where \(\vee\) is coordinatewise maximum.  Hence the edges are naturally
and injectively colored by the middle layer.  (Indeed, their maximum
recovers \(z\), so two colors cannot give the same unordered edge.)

## 2. Degree-two interior

Call a lower-layer vertex exceptional if

\[
    v_t=0\text{ for some }t,qquad v_1=m,
    \quad\hbox{or}\quad v_2=m.                    \tag{2}
\]

Let \(B\) be this exceptional set.  If \(v\notin B\), all four coordinates
are positive and \(v_1,v_2<m\).  The possible middle covers incident to
\(v\) are \(v+e_t\) for those \(t\) with \(v_t<m\).

* For \(t=1\), the chosen pair for \(v+e_1\) is \(\{1,2\}\), and \(v\) is
  the endpoint obtained by subtracting \(e_1\).
* For \(t=2\), the same statement holds with \(e_2\).
* For \(t=3,4\), the chosen pair is still \(\{1,2\}\), because the first
  two coordinates remain positive.  Subtracting \(e_1\) or \(e_2\) cannot
  give \(v=(v+e_t)-e_t\).

Thus

\[
    \deg_G(v)=2\qquad(v\notin B).                 \tag{3}
\]

This checks an important boundary point: the degree is two in the **full**
graph, even when one or both incident edges lead to exceptional vertices.
It follows immediately that every odd-degree vertex and every isolated
vertex of \(G\) belongs to \(B\).

## 3. Component count

Delete the exceptional vertices.  Fix \((v_3,v_4)\).  The remaining
vertices in that fiber are

\[
 (t,,2m-1-v_3-v_4-t,,v_3,,v_4)
\]

over a contiguous integer interval on which both first coordinates lie in
\([1,m-1]\).  The internal selected \(\{1,2\}\)-edges join consecutive
values of \(t\).  Therefore every nonempty fiber induces one path (a
one-vertex path is allowed).  Since \(v_3,v_4\in[1,m]\),

\[
    c(G[V\setminus B])\le m^2.                   \tag{4}
\]

Adding the vertices of \(B\), with all their incident edges, can merge old
components and can create at most one new component per added vertex.  Thus

\[
    c(G)\le m^2+|B|.                              \tag{5}
\]

The fallback rule for a middle point with \(z_1z_2=0\) is irrelevant to
(3)--(5): every endpoint of such an edge has a zero first or second
coordinate and is already exceptional.

For a crude explicit estimate, union-bound the six exceptional
hyperplanes.  Each equation \(v_t=0\) has at most
\(\binom{2m+1}{2}\) nonnegative solutions before imposing the upper bounds.
Each equation \(v_1=m\) or \(v_2=m\) has exactly
\(\binom{m+1}{2}\) unrestricted residual solutions (the upper bounds are
automatic because their sum is \(m-1\)).  Hence

\[
 |B|\le4\binom{2m+1}{2}+2\binom{m+1}{2}
      =9m^2+5m.                                   \tag{6}
\]

Overlaps only improve this bound.

## 4. Euler-trail conversion

Every nontrivial connected component with \(o\) odd vertices has an
edge-disjoint decomposition into

\[
    \max(1,o/2)
\]

trails.  This is the standard Euler argument: pair the odd vertices with
temporary edges, take an Euler circuit, and cut at the temporary edges; an
Eulerian component needs one closed trail.

Write each trail as its vertex sequence and concatenate all these sequences
in arbitrary order.  Append every isolated vertex as a singleton.  If
\(T\) is the number of nonempty trails, \(O\) the number of odd vertices,
and \(I\) the number of isolated vertices, the resulting word has length

\[
    |E(G)|+T+I.                                   \tag{7}
\]

Every lower vertex occurs either on a trail or in the appended isolated
list, so all of \(V\) occurs as singleton values.  Every graph edge occurs
as a consecutive pair within exactly one trail, and (1) gives all of \(Z\)
among the adjacent maxima.  New adjacent pairs created when trail words are
concatenated have arbitrary extra maxima, which are harmless: coverage is
monotone and does not demand uniqueness.

Since \(|E(G)|=|Z|\), while \(O,I\le|B|\), and

\[
 T\le c_{\rm nontriv}(G)+O/2\le m^2+|B|+O/2,
\]

(6)--(7) give

\[
 \begin{aligned}
 |W|&\le |Z|+m^2+\frac52|B|\\
     &\le |Z|+\frac{47}{2}m^2+\frac{25}{2}m.
 \end{aligned}                                   \tag{8}
\]

No connectivity assumption on \(G\), and no special choice in the fallback
rule, is needed.

## 5. A bonus triangular upper shadow

The same word can be made to cover more than the two layers stated in the
theorem.  Choose the Euler decomposition so that trails are cut only at odd
vertices (and, in an Eulerian component, start at an exceptional vertex).
All odd vertices are exceptional.  Moreover every component contains an
exceptional vertex: an endpoint of any finite nonexceptional fiber path has
its remaining full-graph edge leaving that path.  Hence every
nonexceptional degree-two fiber path is traversed as one contiguous segment.

Fix \((c,d)=(v_3,v_4)\) and put

\[
    K=2m-1-c-d.
\]

If the corresponding nonexceptional fiber has parameter interval
\([L,U]\), its word segment, in one orientation or the other, is

\[
    v_t=(t,K-t,c,d),\qquad L\le t\le U.
\]

For \(L\le a\le b\le U\), the maximum of the subsegment from \(v_a\) to
\(v_b\) is

\[
    (b,K-a,c,d).                                  \tag{9}
\]

Thus that single fiber automatically covers the triangular family

\[
 \{(x,y,c,d):L\le x\le U,
                 K-U\le y\le K-L,
                 x+y\ge K\}.                     \tag{10}
\]

This bonus does not cover the whole upper ideal, but it is potentially
useful for the next construction step: the trail skeleton already carries
an exact family of longer-window shadows, rather than only its edge colors.

## 6. Unequal fixed-dimensional boxes

Let

\[
    P=\prod_{i=1}^D[0,\ell_i],\qquad
    S=\sum_i\ell_i,qquad r=\lfloor S/2\rfloor,
\]

and choose two distinguished coordinates \(p,q\) with positive capacities.
For each \(z\in P_r\) having at least two positive coordinates, use
\(\{p,q\}\) when \(z_p,z_q>0\), and otherwise any fixed pair of positive
coordinates.  Make the same edge between the two corresponding lower
covers.

Define

\[
 B=\{v\in P_{r-1}:v_i=0\text{ for some }i,
                       \text{ or }v_p=\ell_p,
                       \text{ or }v_q=\ell_q\}.
\]

Exactly the same incidence check gives degree two outside \(B\).  After
deleting \(B\), fixing the other \(D-2\) coordinates leaves one contiguous
path in the \((p,q)\)-fiber.  Consequently

\[
c(G[P_{r-1}\setminus B])
 \le\prod_{i\ne p,q}(\ell_i+1)=O_D(S^{D-2}).      \tag{11}
\]

Each exceptional hyperplane is a rank slice in a \((D-1)\)-dimensional
box, and the unrestricted stars-and-bars bound gives

\[
 |B|\le(D+2)\binom{S+D-2}{D-2}=O_D(S^{D-2}).      \tag{12}
\]

There are at most \(D\) middle points supported on a single coordinate.
Append these literally.  All other middle points supply one graph edge.
The edge deficit and the literal additions cancel in the leading count, so
the Euler-trail argument yields

\[
    |W|=|P_r|+O_D(S^{D-2}).                        \tag{13}
\]

The degenerate cases with fewer than two positive-capacity coordinates are
one-dimensional and can be handled directly; they are not part of the
high-dimensional asymptotic application.

## 7. Scope and remaining gap

The audit validates all four claims posed:

1. every nonexception lower vertex has degree exactly two;
2. components, odd vertices, and isolates are all \(O(m^2)\);
3. Euler-trail concatenation has length \(|P_{2m}|+O(m^2)\);
4. singleton and adjacent-window maxima cover the two specified layers.

The theorem is stronger than a numerical experiment and is uniform in the
box side lengths for fixed dimension.  Its limitation is equally precise:
longer windows of the trail word are uncontrolled.  Turning this two-layer
word into a full-box word with only \(o(S^{D-1})\) additional entries
requires a new mechanism that makes the Euler trails simultaneously carry
the remaining lower and upper ranks.  One promising formulation is to
choose the edge-selection rule and the order of the Euler trails so that
their longer coordinatewise maxima form prescribed shadow paths; that is a
strictly stronger problem than the theorem proved here.

As a non-proof sanity check, I also exhaustively generated the graph for
every \(1\le m\le12\), using the lexicographically first available fallback
pair.  In every case all nonexceptional degrees were exactly two, every odd
or isolated vertex was exceptional, every edge recovered its prescribed
middle color by coordinatewise maximum, and the component bound (5) held.
The proof above, rather than this finite check, establishes the theorem.
