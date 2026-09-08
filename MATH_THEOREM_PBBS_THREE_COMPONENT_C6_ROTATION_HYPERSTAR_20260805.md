# Rotation rigidity of the explicit three-component PBBS connector

**Date:** 2026-08-05  
**Method:** rooted-Dyck enumeration and cyclic action-angle bookkeeping; no
computation or search  
**Status:** unconditional.  All cyclic translates of the explicit
three-component q2-neutral C6 project to the **same** component triple.
Thus rotation supplies many literal placements but no component-level
expansion.  This is an exact rotation-rigidity result, not a spanning
hyperstar theorem.

## 1. The `(m-1,1)` action sector has one component

For a rooted Dyck word with soliton partition `(m-1,1)`, the peak-pruning
profile is

\[
                         (2,1,\ldots,1).
\tag{1.1}
\]

There are exactly `2m-3` rooted Dyck words with this profile.  Indeed such
a word has exactly two peaks, so write it as

\[
                         1^a0^b1^c0^d
\tag{1.2}
\]

with positive exponents.  Deleting the two peaks must leave the mountain
`1^(m-2)0^(m-2)`.  Therefore either `b=1`, merging the two one-runs, or
`c=1`, merging the two zero-runs.  The complete list, with the common word
counted once, is

\[
 A_j=1^{m-1}0^j1\,0^{m-j}\qquad(1\le j\le m-1),
\]

\[
 B_j=1^j0\,1^{m-j}0^{m-1}\qquad(1\le j\le m-2).
\tag{1.3}
\]

The rooted PBBS map satisfies

\[
 A_j\xrightarrow{m-1}B_j\xrightarrow{m+1}A_{j+1}
 \quad(1\le j\le m-2),
 \qquad
 A_{m-1}\xrightarrow{m-1}A_1.
\tag{1.4}
\]

Thus all shapes in the action sector form one shape cycle of length

\[
                         p=2m-3.
\]

Its voltage is

\[
 (m-1)^2+(m-2)(m+1)
   =(m-2)(2m+1)+1,
\tag{1.5}
\]

so it is one lifted `f`-cycle of length `(2m+1)(2m-3)`.  This length is
odd, hence it is also one `g=f^2` factor component.  Denote it by
`T`.  Ground rotation acts on it as

\[
 \rho=f^p=g^{p(m+1)}.
\tag{1.6}
\]

In particular `rho(T)=T`.

## 2. Exact rotation triples

Let `E_0` be the explicit three-component q2-neutral C6 with action
profiles

\[
 \lambda_A=(m-2,1,1),\qquad
 \lambda_B=(m-2,2),\qquad
 \lambda_T=(m-1,1).
\tag{2.1}
\]

Let `A_0,B_0,T` be the three PBBS components containing its old edges, and
put

\[
 A_k=\rho^kA_0,qquad B_k=\rho^kB_0
 \quad(k\in\mathbb Z/(2m+1)).
\tag{2.2}
\]

PBBS and the max-height section commute with `rho`, so `rho^kE_0` is again
a selected q2-neutral three-component clean C6.  Its exact projected
component triple is

\[
                         \boxed{\{A_k,B_k,T\}}.
\tag{2.3}

Let

\[
 a=|\{A_k\}|,qquad b=|\{B_k\}|.
\tag{2.4}
\]

Both `a` and `b` divide `2m+1`.  In action-angle terms, if the rooted shape
cycles containing the displayed A and B states have voltages `v_A,v_B`,
then

\[
 a=\gcd(v_A,2m+1),qquad
 b=\gcd(v_B,2m+1).
\tag{2.5}
\]

Indeed a shape cycle of voltage `v` lifts to `gcd(v,n)` physical
`f`-components, and coordinate rotation acts transitively on those
components.  If one such `f`-component has odd length, it is already one
`g=f^2` component.  If it has even length, it splits into two `g`-components;
coordinate rotation has odd order `n`, so it cannot interchange the two
parity classes.  It acts transitively on each of the two resulting families,
again with orbit size `gcd(v,n)`.  Thus (2.5) is valid for the displayed
`g`-components in either parity case.
The number of distinct triples in (2.3) is

\[
                         \operatorname{lcm}(a,b),
\tag{2.6}

which also divides `2m+1`.

### 2.1 The two displayed voltages are units

For the explicit connector these gcds can be evaluated exactly.  Put
`t=m-2`.  Normalizing the states `Z_0` and `Z_1` from the literal gadget at
their unmatched zeros gives the two rooted shapes

\[
 D_A=1^t0^t1010,
 \qquad
 D_B=1100\,1^t0^t.
\tag{2.7}
\]

For `1<=j<=t-1`, put

\[
 X_j=1^t0^j1\,0\,1\,0^{t-j+1},
 \qquad
 Y_j=1^j0\,1\,0\,1^{t-j+1}0^t.
\tag{2.8}
\]

Direct first-maximum complementation gives the shape cycle

\[
 D_A\xrightarrow{t}X_1\xrightarrow{t}Y_1
 \xrightarrow{t+4}X_2\xrightarrow{t}Y_2
 \xrightarrow{t+4}\cdots
 \xrightarrow{t}Y_{t-1}\xrightarrow{t+4}D_A.
\tag{2.9}
\]

It has period `2t-1=2m-5` and voltage

\[
 v_A=t^2+(t-1)(t+4)
     =(t-1)(2t+5)+1
     =(m-3)(2m+1)+1.
\tag{2.10}
\]

For `1<=j<=t-2`, put

\[
 U_j=1^t0^{j+2}1^2 0^{t-j},
 \qquad
 V_j=1^{j+2}0^2 1^{t-j}0^t.
\tag{2.11}
\]

The second shape cycle is

\[
 D_B\xrightarrow{t+4}U_1\xrightarrow{t}V_1
 \xrightarrow{t+4}U_2\xrightarrow{t}V_2
 \xrightarrow{t+4}\cdots
 \xrightarrow{t}V_{t-2}\xrightarrow{t}D_B.
\tag{2.12}
\]

It has period `2t-3=2m-7` and voltage

\[
 v_B=(t-2)(t+4)+(t-1)t
     =(t-2)(2t+5)+2
     =(m-4)(2m+1)+2.
\tag{2.13}
\]

Since `2m+1` is odd, both voltages are units modulo `2m+1`.  Both shape
periods are odd as well.  Consequently each displayed sector lifts to one
`f`-cycle and one `g=f^2` component.  Therefore

\[
                         \boxed{a=b=1}
\tag{2.14}
\]

and every cyclic translate of the connector has exactly the same projected
triple

\[
                         \boxed{\{A_0,B_0,T\}}.
\tag{2.15}
\]

## 3. The rotation block is one hyperedge

Every hyperedge (2.3) is the same hyperedge.  Hence the component
hypergraph generated by all cyclic translates of `E_0` is connected but
has only three vertices:

\[
 \boxed{\text{the rotation family has exactly one connected block}.}
\tag{3.1}

Because the three action profiles differ, these are three distinct
components.  Rotation therefore gives no loose-forest growth at component
level.  Its value is purely positional: it moves the literal support around
the same three cycles.

## 4. Placement on the rigid two-soliton arcs

The T-edge of a rotated connector moves under one coordinate rotation by
`p(m+1)` directed `g`-steps, by (1.6).  As an unordered set of positions,
the `2m+1` rotated copies form one residue class modulo `p`, hence are
spaced every `p` positions around the T-cycle.

The rigid-edge clean C6 cuts T into paths of lengths

\[
                         p(m+1),\qquad pm-2.
\tag{4.1}

For `m>=6`, each open path therefore contains an interior rotated T-edge of
the explicit three-component connector: the rotated positions have maximum
cyclic gap `p`, while both lengths in (4.1) exceed `p`.  Thus the rotation
orbit has T-edge **positional supply on both sides** of the rigid cut.

This does not prove the two-switch escape.  In particular, the rotated
connector has only one old edge on `T`; choosing that edge on one side of
the rigid cut does not simultaneously straddle both resulting `T` paths.
Moreover its other two old edges always remain on the same fixed components
`A_0,B_0`.

## 5. Global scope

The theorem proves one genuine three-component connector and a full cyclic
family of its physical placements, but that family is only one projected
hyperedge.  It does not show that any further PBBS component belongs to the
same connector block, nor that the full common-pivot connector hypergraph
has `O(1)` blocks.  Further expansion requires a connector with a different
action-angle triple, not merely another cyclic translate of this one.
