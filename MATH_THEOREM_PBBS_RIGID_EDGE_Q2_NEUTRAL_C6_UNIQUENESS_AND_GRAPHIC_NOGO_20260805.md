# Every q2-neutral clean `C6` through the rigid PBBS edge is graphic-neutral

**Date:** 2026-08-05  
**Method:** exact rooted-height inequalities and the common-deletion
classification; no computation or search  
**Status:** unconditional for `m>=4`.  Up to cyclic relabelling and reversal,
there is only one q2-transparent clean `C6` through a single-soliton PBBS
edge.  Its two companion edges necessarily lie on the same completely
selected two-soliton component.  Hence no single clean `C6` can repair the
PBBS graphic obstruction.

## 1. General clean-C6 hypotheses

Let `P_0Q_0` be one directed edge of the PBBS single-soliton component on
`Z/(2m+1)Z`.  Suppose a clean common-core `C6` uses old edges

\[
 P_iQ_i\qquad(i\in\mathbb Z/3),                    \tag{1.1}
\]

with q1 rows

\[
 R_i=K+a_i,qquad
 P_i=K+a_i+a_{i+1},qquad
 Q_i=K+a_i+c,                                      \tag{1.2}
\]

where `|K|=m-2` and `a_0,a_1,a_2,c` are pairwise distinct outside `K`.
Assume:

1. all three old edges are directed PBBS edges `P_i -> Q_i`;
2. all six old q1 occurrences needed at the `P_i` coexist in the
   one-occurrence max-height section; and
3. replacing `P_iQ_i` by `P_iQ_(i+1)` preserves the selected q2 multiset.

The exact common-deletion theorem then gives one `d in K` such that the
unchanged other q1 row at every `P_i` is

\[
 L_i=P_i-d.                                        \tag{1.3}
\]

For a directed PBBS edge, the rooted two-step formula identifies

\[
 r_+(P_i)=c,qquad p_+(P_i)=a_{i+1},qquad
 p_-(P_i)=d,                                       \tag{1.4}
\]

where `p_+` and `p_-` are the forward and backward distinguished
deletions of the rooted Dyck word.

## 2. Normalize the rigid edge

Cyclically relabel so that

\[
 c=0,qquad P_0=\{1,2,\ldots,m\}.                  \tag{2.1}
\]

Its rooted Dyck word is the mountain `1^m0^m`.  Therefore

\[
 d=p_-(P_0)=1,qquad a_1=p_+(P_0)=m.               \tag{2.2}
\]

Since `P_0=K+a_0+a_1`, write

\[
 a_0=s\in\{2,\ldots,m-1\}.                        \tag{2.3}
\]

The remaining active label is outside `P_0`, so, in the rooted linear
order,

\[
 a_2=t\in\{m+1,\ldots,2m\}.                       \tag{2.4}
\]

## 3. The forward-deletion constraints force `t=m+1` and `s=m-1`

The state

\[
 P_1=(P_0-s)+t                                    \tag{3.1}
\]

is obtained from the mountain by changing the up-step at `s` to a
down-step and the down-step at `t` to an up-step.  Before `t`, its largest
height is `m-2`: at time `m` the missing up-step has reduced the mountain
height from `m` to `m-2`, and the earlier height `s-1` is no larger.

After the step at `t`, direct counting gives height

\[
 h_{P_1}(t)=2m-t.                                  \tag{3.2}
\]

Equation (1.4) requires `t=a_2` to be the **first** up-step reaching the
global maximum of `P_1`.  Hence

\[
 2m-t>m-2.
\]

Together with `t>=m+1`, this forces

\[
                         \boxed{t=m+1}.             \tag{3.3}
\]

Now

\[
 P_2=(P_0-m)+(m+1)                                 \tag{3.4}
\]

has rooted word

\[
 1^{m-1}0,1,0^{m-1}.                             \tag{3.5}
\]

Its global height is `m-1`, first reached at coordinate `m-1`; the later
up-step at `m+1` only ties that height.  Equation (1.4) requires
`a_0=s` to be this first distinguished up-step.  Therefore

\[
                         \boxed{s=m-1}.             \tag{3.6}
\]

Equations (2.2), (3.3), and (3.6) recover uniquely

\[
 K=\{1,\ldots,m-2\},quad
 (a_0,a_1,a_2,c)=(m-1,m,m+1,0).                   \tag{3.7}
\]

Reversal gives the only opposite orientation.

## 4. Forced component geometry

For the unique data (3.7), the two companion owners have rooted shapes

\[
 P_2:\ 1^{m-1}010^{m-1},
 \qquad
 P_1:\ 1^{m-2}0110^{m-1}.                         \tag{4.1}
\]

The explicit rooted-shape cycle

\[
 A_j=1^{m-1}0^j1,0^{m-j},qquad
 B_j=1^j0,1^{m-j}0^{m-1}                         \tag{4.2}
\]

satisfies

\[
 A_j\to B_j\to A_{j+1},qquad A_{m-1}\to A_1.   \tag{4.3}
\]

It has shape period `2m-3` and physical voltage one.  Hence it lifts to a
single PBBS component, and (4.1) are two phases of that same component.
The max-height block calculation gives outgoing block heights at most

\[
 (m-2,1,0)
\]

up to cyclic order, so for `m>=4` the whole component is selected.

The exact cut-and-reconnect calculation for (3.7) then shows that the old
single-soliton cycle and this two-soliton cycle are replaced by two cycles,
all of whose q1 positions remain selected.

### Theorem 4.1 (one-C6 graphic no-go)

For `m>=4`, every q2-multiset-preserving clean common-core `C6` through a
directed single-soliton PBBS edge is, up to cyclic relabelling and reversal,
the unique gadget (3.7).  It is q1-, upper-q1-, and q2-transparent, but it
does not decrease the number of completely selected components.

Therefore a graphic repair requires at least one of:

1. two coupled clean `C6` switches;
2. a higher-support alternating circuit; or
3. an A/Z Pascal connector not representable by one clean `C6`.

## 5. Dependencies and scope

The proof uses the exact clean-C6 common-deletion classification and the
rooted PBBS distinguished-deletion formula.  Section 4 uses the separately
audited two-soliton shape cycle and cut-and-reconnect identities.

The theorem is a no-go only for one q2-transparent clean common-core `C6`
through the rigid edge.  It does not exclude two switches, a non-common-core
larger circuit, or a direct Pascal-sector repair.
