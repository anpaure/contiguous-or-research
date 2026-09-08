# Independent audit: protected upper-exact Hamilton path and rooted-tail extension

Date: 2026-08-01  
Lane: protected Catalan connector / additive-one owner layer  
Audited source:
`MATH_THEOREM_PROTECTED_UPPER_EXACT_HAMILTON_PATH_AND_ROOTED_TAIL_EXTENSION_20260801.md`  
Status: **GO after two scope corrections**.  The Kruskal--Katona surplus,
the protected Hall extension through `t=m`, and the Hamilton-path/Catalan
decomposition are correct.  Global upper-colour distinctness across a
multi-packet bank is an additional hypothesis; the contracted connector is
a directed free-port Hamilton path, not an arbitrary unlabelled tree.

## 1. Executive verdict

Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m.
\]

The audited theorem proves exactly the following unconditional statements.

1. For fixed perfect `M0`, a matching `Q subset ML_m-M0` of size `W-1`
   gives an alternating Hamilton path exactly when its labelled rooted links
   are graphic-independent.  Adjacent-upper surjectivity is exactly
   `up(Q)=binom([2m-1],m+1)`.
2. Choosing one edge of each upper colour gives a `C`-component rooted
   path forest `Q0`; the remaining `C-1` edges must connect the components
   as one directed free-port Hamilton path.  There is no residual closure.
3. Every nonempty family `X` of rank-`m+1` sets has

   \[
       |\partial X|\ge |X|+m.
   \]

   Consequently any `t<=m` distinct upper/tail tickets extend to a full
   upper-to-tail containment injection.

The last object is only a semimatching in the original incidence graph:
the forced opposite heads may collide, and even a head-injective choice need
not be graphic-independent.  Those are real remaining rows.

## 2. Audit of the central-shadow surplus

Set `k=m+1` and `x=|X|`.  Kruskal--Katona reduces the question to the
initial colex segment.  Since

\[
 1\le x\le {2k-3\choose k},
\]

write its first colex block as

\[
 x={s\choose k}+b,
 \qquad k\le s\le2k-3,
 \qquad 0\le b<{s\choose k-1}.
\]

The numerical shadow recursion is exactly

\[
 \partial_k(x)={s\choose k-1}+\partial_{k-1}(b).
\]

The remainder is a family of `(k-1)`-sets on at most `s<=2k-3` points.
The normalized matching inequality gives

\[
 |\partial\mathcal B|
 \ge |\mathcal B|
       {{s\choose k-2}\over {s\choose k-1}}
 \ge |\mathcal B|,
\]

because `{s choose k-2}>={s choose k-1}` in this range.  Hence
`partial_(k-1)(b)>=b`.

For

\[
 D_s={s\choose k-1}-{s\choose k},
\]

one has `D_k=k-1` and

\[
 D_{s+1}-D_s={s\choose k-2}-{s\choose k-1}\ge0
 \quad(k\le s\le2k-3).
\]

Therefore

\[
 \partial_k(x)-x
 =D_s+\partial_{k-1}(b)-b
 \ge k-1=m.
\]

This verifies Lemma 2.1.  It is sharp: a singleton upper family has a
lower shadow of size `m+1`, hence surplus exactly `m`.

## 3. Audit and sharpness of the protected Hall extension

Delete the `t` prescribed upper vertices and the `t` prescribed rank-`m`
tails.  For every nonempty remaining upper family `X`,

\[
 |N(X)\setminus T(P)|
 \ge |N(X)|-t
 \ge |X|+m-t
 \ge |X|.
\]

Hall therefore saturates all remaining upper vertices, and adjoining the
prescribed pairs gives the claimed containment injection.  No approximate
or asymptotic step occurs.

The universal threshold `t<=m` is best possible for arbitrary prescribed
tickets when `m>=3`.  Fix an `(m+1)`-set `R_0` and a point `b` outside it.
For every one of the `m+1` facets `T` of `R_0`, prescribe

\[
             (R_T,T),\qquad R_T=T\cup\{b\}.
\]

The `R_T` and the `T` are separately distinct, but after their deletion the
unprescribed upper vertex `R_0` has no available tail.  Thus `t=m+1` cannot
be guaranteed.

## 4. Incidence lift and head-collision scope

For a selected containment pair `(R,T)`, put

\[
 L=M_0^{-1}(T),\qquad T=L\cup\{a\},\qquad
 R=T\cup\{b\},\qquad V=L\cup\{b\}.
\]

Then `LV` is the unique other incidence corner of `[L,R]` and

\[
 \operatorname {up}(LV)=M_0(L)\cup V=T\cup V=R.
\]

Distinct `T` give distinct rooted link tails `L`.  They do not force the
middle heads `V` to be distinct.  Accordingly the Hall theorem produces
exactly an upper-exact rooted-tail semimatching.  Promoting it to `Q0`
still requires the head partition constraint and graphic acyclicity in the
same choice.

Terminology warning: `T=M0(L)` is the root-owner/tail ticket, whereas the
directed link itself has contracted tail vertex `L`.  The bijection `M0`
makes these descriptions equivalent, but they should not be conflated when
checking physical head collisions.

## 5. Hamilton path and Catalan decomposition

Contracting `M0` turns `M0 union Q` into `lambda(Q)` on `W` vertices.  A
graphic-independent `W-1`-edge link set is a spanning tree.  Since `Q` is
a matching, every contracted vertex has indegree and outdegree at most one;
the tree therefore has maximum undirected degree two and is one spanning
path.  Expansion recovers the alternating Hamilton path.

Selecting one representative of every upper colour gives

\[
 |Q_0|=U=W-C,
 \qquad c(\lambda(Q_0))=W-U=C,
 \qquad |Q_1|=C-1.
\]

Each `Q0` component is a coherently directed path with one free outgoing
and one free incoming port.  Matching compatibility forces every `Q1`
connector to use such free ports.  Hence after contraction `Q1` is not an
arbitrary tree: it is a directed Hamilton path through the `C` components.
This is equivalent to a spanning tree only while the endpoint partition
constraints are retained.

This agrees with
`MATH_AUDIT_K_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md` and its
source-cell ledger.  In particular, no residual matching or closure edge
exists at additive one, but the direct source architecture still needs one
controlled boundary nonowner among the `W+1` depth-row cells.

## 6. Protected pivot-bank correction

One collared pivot path has `3h` Johnson transitions and `3h` short-shore
incidences.  Its immediate-upper labels are distinct *within that path*.
For `H` copies, owner/lower-colour resource disjointness makes the rooted
tails distinct, but it does not imply that upper labels from different
copies are distinct.

Therefore Theorem 2.2 applies to all `3Hh` protected tickets only under the
extra hypothesis

\[
 \operatorname {up}(P_1)\text{ is globally injective across the bank}.
\]

Under that hypothesis and `3Hh<=m`, the Hall row closes.  The stronger
small protected-factor bound `6Hh<=m-2` supplies the numerical inequality
and a compatible alternating perfect class, but by itself does not supply
cross-packet upper distinctness, head injectivity, or the directed Catalan
connector.

Likewise, the statement `P1 subset Q0` is conditional on an already existing
protected certificate `Q`: then one chooses each protected occurrence as
the representative of its globally distinct colour.  It is not an
existence proof for `Q`.

## 7. Final audited frontier

After the corrections above, the exact protected owner-layer frontier is

\[
 \boxed{
 \begin{gathered}
 \text{globally upper-distinct protected rooted-tail transversal}\\
 +\ \text{simultaneous opposite-head injection}\\
 +\ \text{directed free-port Catalan connector path}.
 \end{gathered}}
\]

The KK/Hall theorem removes the first marginal row through `t=m`; it does
not solve the last two correlated rows.  Exterior residence, arbitrary-
width upper witnesses, the literal common cap, and regeneration remain
outside this owner/q1 audit.  No unconditional `B+1`, `B+O(1)`, or exact
all-dimensional conclusion follows.
