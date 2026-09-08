# A normalized common-base three-packet rainbow obstruction for `d>=4`

Date: 2026-08-01  
Status: proved only under the normalized common-base depth-two hypothesis in
Section 2.  The earlier arbitrary-core classification claim is **not
proved**: an adjacent Johnson edge has multiple square decompositions at
higher rank.  This note therefore does not establish a no-go for every
canonical packet triple.

## 1. Statement

For a canonical mixed-screen packet write

\[
 C=K\cup\{\infty,c\},\qquad
 \pi=(g_1,\ldots,g_d),
\]

and let `(a,b)` be its ordered active pair.  At depth `q`, with
`t=d+1-q`, its new-minus-old lower action is

\[
 \Delta_q=
 e_{C a P_t}-e_{C b P_t}+e_{C b S_t}-e_{C a S_t},       \tag{1.1}
\]

where `P_t={g_1,...,g_t}` and `S_t={g_{d-t+1},...,g_d}`.
The packet also has the two mandatory lower-`q1` socket colours

\[
 C\cup\{a,g_1,\ldots,g_d\},\qquad
 C\cup\{b,g_1,\ldots,g_d\}.                            \tag{1.2}
\]

### Theorem 1.1 (normalized common-base scope)

Let `d>=4`.  Three nontrivial canonical mixed-screen packets of one rank,
whose depth-two squares already satisfy one of the two normalized
common-base forms in Section 2 cannot satisfy simultaneously

1. `Delta_q^0+Delta_q^1+Delta_q^2=0` for every `2<=q<=d`; and
2. pairwise-disjoint complete lower-`q1` palettes.

Consequently the four-packet twisted cube is minimal in this normalized
three-square face.  Minimality in the full arbitrary-core canonical
catalogue remains open.

The threshold is sharp.  For `d=2,3`, the three filler words

\[
 (x,M,y),\quad(y,M,z),\quad(z,M,x),                    \tag{1.3}
\]

with one common active pair, where `M` is empty for `d=2` and is a singleton
for `d=3`, give a literal three-packet cancellation.  Private outer padding
fillers and private `e,delta` roles make their complete owner and lower-`q1`
palettes pairwise disjoint.

## 2. Normalized depth-two hypothesis and the open classification gate

At depth two (1.1) is a Johnson square

\[
 e_{Hax}+e_{Hby}-e_{Hbx}-e_{Hay},                    \tag{2.1}
\]

where

\[
 H=C\cup\{g_2,\ldots,g_{d-1}\},\quad x=g_1,\ y=g_d.
\]

The theorem assumes that, after literal relabelling, the three depth-two
squares have one of the following forms.

* **Rectangle triangle.**  Their six support atoms are

  \[
       H\cup\{p_i,q_j\},\qquad i\in\{0,1\},\quad
       j\in\{0,1,2\},                                  \tag{2.2}
  \]

  and the three squares are the rectangles on the three pairs of `q` labels.

* **Diagonal Pluecker triangle.**  Their atoms are the six two-subsets of
  four labels over one common base `H`; the three squares are the three
  differences between the three perfect matchings of `K_4`.

These are exactly the two normalized rank-two circuit types enumerated by
the finite audit.  They are **not yet proved exhaustive at arbitrary rank**.
The obstruction is precise: if two rank-`s` sets share a Johnson edge, their
`(s-1)`-intersection contains several possible distinguished labels.
Different squares through that edge can therefore use different
`(s-2)`-bases.  The assertion that every such square has one common `H`
does not follow.  Closing or refuting that higher-rank classification is the
remaining three-packet minimality gate.

## 3. The `q1` socket restriction

In the diagonal case all six packet sockets are facets of the same
`H`-extended four-set.  There are only four such facets, so two sockets, and
hence two complete lower-`q1` palettes, coincide.

In the rectangle case, each rectangle has two possible canonical role
assignments:

* `V`: active pair `{p_0,p_1}` and filler pair `{q_j,q_k}`;
* `H`: filler pair `{p_0,p_1}` and active pair `{q_j,q_k}`.

Two `H` rectangles share a `q` endpoint, and both contain the socket
`H union {p_0,p_1,q}`.  Pairwise palette disjointness therefore permits at
most one `H` rectangle.  Hence only the all-`V` and exactly-one-`H` cases
remain.

## 4. The odd reversal obstruction

For packet `i`, put

\[
 C_i=K_i\cup\{\infty_i,c_i\},\qquad
 \mu_i=(g^i_2,\ldots,g^i_{d-1}).                      \tag{4.1}
\]

The common base `H` in (2.2) satisfies

\[
 H=C_i\mathbin{\dot\cup}\operatorname{set}(\mu_i).  \tag{4.2}
\]

At deepest depth `q=d`, every atom has the form `C_i` plus one `p` and one
`q` label.  Each external pair occurs in exactly two incident rectangles.
Coefficient cancellation therefore matches equal external pairs, and since
`C_i subset H` it forces the two corresponding `C_i` to be equal.  The
rectangle triangle is connected, so

\[
 C_0=C_1=C_2=:C,\qquad
 \operatorname{set}(\mu_0)=\operatorname{set}(\mu_1)
 =\operatorname{set}(\mu_2)=H-C=:M.                  \tag{4.3}
\]

For `0<=s<=|M|`, let `A_i(s)` and `B_i(s)` be respectively the first and
last `s` labels of `mu_i`, as sets.

In the all-`V` case orient the filler edges cyclically as

\[
 (q_0,\mu_0,q_1),\quad(q_1,\mu_1,q_2),\quad
 (q_2,\mu_2,q_0).                                    \tag{4.4}
\]

At every intermediate depth, equality at the columns labelled `q_0,q_1,q_2`
gives

\[
 A_0(s)=B_2(s),\qquad A_1(s)=B_0(s),\qquad
 A_2(s)=B_1(s)                                       \tag{4.5}
\]

for every `s`.  Equality of all nested prefix and suffix sets is equality of
the corresponding ordered words, so

\[
 \mu_0=\operatorname{rev}(\mu_2),\quad
 \mu_1=\operatorname{rev}(\mu_0),\quad
 \mu_2=\operatorname{rev}(\mu_1).                   \tag{4.6}
\]

Thus `mu_0=rev(mu_0)`.

In the exactly-one-`H` case take that rectangle on `q_0q_1`, oriented as

\[
 +p_0q_0A_H-p_0q_1A_H+p_1q_1B_H-p_1q_0B_H.          \tag{4.7}
\]

Orient the two `V` rectangles on `q_1q_2` and `q_2q_0` so that their
depth-two sum cancels (4.7).  At an intermediate layer the coefficients of
`p_0q_0,p_0q_1,p_1q_1` give respectively

\[
 A_H(s)=B_{20}(s),\qquad A_{12}(s)=A_H(s),\qquad
 B_H(s)=A_{12}(s).                                   \tag{4.8}
\]

Thus `A_H(s)=B_H(s)` for every `s`, and again
`mu_H=rev(mu_H)`.

A word of distinct labels equal to its reversal has length at most one.
But `|M|=d-2>=2`, a contradiction in both remaining cases.  This proves
Theorem 1.1.  \(\square\)

## 5. Scope boundary

The proof uses the canonical formula (1.1), its canonical sockets (1.2), and
the normalized common-base hypothesis of Section 2.  Within that face it
allows arbitrary filler orders and proves the sharp `d=4` threshold.  It
does not cover arbitrary-core square triples, representative-changing
moves, or the authenticated one-block-order reflection breaker.  Thus it
is an exact normalized obstruction, not canonical four-packet minimality.

## 6. Finite boundary audit

The dependency-free audit enumerates the normalized signed-square circuits
on five labels, verifies the `K_(2,3)` and `K_4` types, tests socket choices,
and literally replays the sharp `d=2,3` exceptions and the first failure at
`d=4`:

```text
scratch/audit_ad_normalized_common_base_three_packet_rainbow_no_go_20260801.py
scratch/ad_normalized_common_base_three_packet_rainbow_no_go_20260801.audit.json
```

It reports

```text
PASS_AD_NORMALIZED_COMMON_BASE_THREE_PACKET_RAINBOW_NO_GO
```

and explicitly records `arbitrary_core_classification=UNPROVED`.  Its
canonical payload SHA-256 is

```text
1b635e2fd0a7f245b4bbbdb0a0730493782641a998bd0a27e67c8b8901a2b9db
```
