# Fully flaggable overlapping-core pivot bridges

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local theorem.  The pivot bridge can be realized
with a full strict suffix flag on every bridge owner, with all flag values
inside one bridge distinct.  Its exact rank histogram is concentrated in
the lower-central band.  This removes the *local* lower-slot loss from the
pivot gluing theorem.  It does not select Catalan-many bridges with mutually
disjoint named flag decks, nor construct the protected trace factor on their
complement.

## 1. Data and source letters

Fix integers

\[
                 2\le h\le r-2,\qquad k\ge r+h,
\tag{1.1}
\]

and choose pairwise disjoint objects

\[
 Q,\quad \lambda _1,\ldots,\lambda _h,\quad
 \rho _1,\ldots,\rho _h,
 \qquad |Q|=r-h.                                  \tag{1.2}
\]

The displayed Greek symbols denote singleton coordinates.  Choose distinct
coordinates `a,b in Q` and put

\[
                 C=Q-\{a\},\qquad X=Q-\{b\}.       \tag{1.3}
\]

Thus

\[
 |C|=|X|=r-h-1,\qquad C\cup X=Q,
 \qquad X-C=\{a\},\quad C-X=\{b\}.               \tag{1.4}
\]

Define the two order-`h` rail states

\[
 U_i=C\cup\{\lambda_i\},\qquad
 V_i=C\cup\{\rho_i\}\qquad(1\le i\le h).        \tag{1.5}
\]

Starting from `U=(U_1,...,U_h)`, append the `h+1` nonempty letters

\[
                         X,V_1,\ldots,V_h.          \tag{1.6}
\]

## 2. The owner geodesic is unchanged

### Proposition 2.1

The `h+1` length-`h+1` windows traversed by (1.6) have unions

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
                    \qquad 0\le j\le h.           \tag{2.1}
\]

They are distinct rank-`r` owners and form the Johnson geodesic

\[
 M_{j+1}=M_j-\{\lambda_{j+1}\}+\{\rho_{j+1}\}.
\tag{2.2}
\]

After all appends, the final order-`h` state is exactly
`V=(V_1,...,V_h)`.

#### Proof

After `X` and the first `j` letters of `V` have been appended, the current
window consists of

\[
 U_{j+1},\ldots,U_h,X,V_1,\ldots,V_j.
\]

Every `U_i` and `V_i` contains `C`, while `C union X=Q`.  The remaining
coordinates are precisely the lambda suffix and rho prefix in (2.1).
Equation (1.2) gives rank `r`, and (2.2) follows immediately.  After the
last append, the last `h` letters are `V_1,...,V_h`.  `square`

## 3. Every bridge owner has a full strict flag

For `0<=j<=h` and `1<=ell<=h`, let `S_(j,ell)` be the union of the final
`ell` source letters in the window whose owner is `M_j`.

### Theorem 3.1 (full flag and exact formulas)

For `j=0`,

\[
 S_{0,1}=X,                                        \tag{3.1}
\]

and, for `2<=ell<=h`,

\[
 S_{0,\ell}
   =Q\cup\{\lambda_{h-\ell+2},\ldots,\lambda_h\}.
\tag{3.2}
\]

For `1<=j<=h`,

\[
 S_{j,\ell}
 =C\cup\{\rho_{j-\ell+1},\ldots,\rho_j\}
       \qquad(1\le\ell\le j),                    \tag{3.3}
\]

while, for `j+1<=ell<=h`,

\[
 S_{j,\ell}
 =Q\cup\{\rho_1,\ldots,\rho_j\}
       \cup\{\lambda_{h-(\ell-j-1)+1},\ldots,\lambda_h\},
\tag{3.4}
\]

where an empty lambda range is omitted.  Equivalently, the lambda suffix in
(3.4) has length `ell-j-1`.

For every fixed `j`,

\[
 S_{j,1}\subsetneq S_{j,2}\subsetneq\cdots
       \subsetneq S_{j,h}\subsetneq M_j.          \tag{3.5}
\]

Hence every bridge owner carries all `h` possible strict proper-suffix
cells.

#### Proof

For `j=0`, the window is

\[
 U_1,\ldots,U_h,X.
\]

The one-letter suffix is `X`.  The next suffix adds `U_h=C union
{lambda_h}`; since `C union X=Q`, this gives `Q union {lambda_h}`.
Every further step adds the next unused lambda coordinate, proving
(3.1)--(3.2) and strictness.

For `j>=1`, the current window is

\[
 U_{j+1},\ldots,U_h,X,V_1,\ldots,V_j.
\]

While the suffix remains inside `V_1,...,V_j`, its union is (3.3), and
each step adds one new rho coordinate.  The next step adds `X`.  Since the
existing union contains `C` and `X-C={a}`, this step is strict and changes
the common core from `C` to `Q`.  Every later step adds one unused lambda
coordinate, giving (3.4).  A proper suffix omits the first letter of its
owner window: for `j<h` it omits `U_(j+1)` and hence lambda_(j+1), while
for `j=h` it omits `X` and hence the coordinate `a`.  Thus the last
containment in (3.5) is also strict.  `square`

## 4. No collision occurs inside one bridge

### Theorem 4.1 (internal target distinctness)

The `h(h+1)` sets

\[
                    \{S_{j,\ell}:0\le j\le h,
                                      1\le\ell\le h\}
\tag{4.1}
\]

are pairwise distinct.

#### Proof

The exceptional value `S_(0,1)=X` contains `a` but not `b`.  Every value in
(3.2) contains all of `Q`, while every value in (3.3) contains `b` but not
`a`; hence `S_(0,1)` collides with neither family.

Values in (3.3) are determined by the nonempty rho interval

\[
                         \{\rho_{j-\ell+1},\ldots,\rho_j\}.
\]

Its right endpoint is `j` and its length is `ell`, so these values are
pairwise distinct.

Every value in (3.2) or (3.4) contains all of `Q`.  A value in (3.4) with
`j>=1` has the nonempty rho prefix `rho_1,...,rho_j`, which determines `j`;
a value in (3.2) has no rho coordinate and corresponds uniquely to `j=0`.
After `j` is known, the lambda suffix length determines `ell`.  Thus the
`Q`-containing values are pairwise distinct.  Finally, a value containing
`Q` cannot equal a value from (3.3), which omits `a`.  This exhausts all
cases.  `square`

## 5. Exact rank histogram

### Corollary 5.1

One overlapping-core bridge supplies exactly

\[
 \boxed{
  1\text{ target of rank }r-h-1;
  \quad h\text{ targets of rank }r-h;
  \quad h+1\text{ targets of every rank }r-h+1,\ldots,r-1.
 }
\tag{5.1}
\]

#### Proof

For `j=0`, equation (3.1) has rank `r-h-1`, while (3.2) has ranks

\[
                         r-h+1,\ldots,r-1.
\]

For every `1<=j<=h`, equations (3.3)--(3.4) together give one set at each
rank

\[
                         r-h,r-h+1,\ldots,r-1.
\]

Summing over `j` proves (5.1).  The count is

\[
 1+h+(h-1)(h+1)=h(h+1),
\]

as required by Theorem 4.1.  `square`

Thus the bridge does not force a low-rank singleton rail.  All its natural
targets lie in the lower-central band, apart from the single rank
`r-h-1` value, and every bridge owner retains full suffix capacity.

## 6. Consequence and exact remaining gate

Replace the conservative pivot letters in the Catalan-scale trace-factor
gluing theorem by (1.3)--(1.6).  The owner geodesic and zero-extra-length
concatenation are unchanged, while the local raw lower-slot charge per
bridge drops from `h(h+1)` to zero.

This is a local statement.  To use all bridge flags globally one still has
to choose the bridge modules so that their natural decks (4.1) are mutually
target-disjoint and disjoint from the component flags.  For `m` bridges the
required rank counts are exactly

\[
 m,\quad hm,\quad (h+1)m,\ldots,(h+1)m             \tag{6.1}
\]

on the ranks in (5.1).  At the standard central Catalan scale
`k=2r+O(1)`, `m=Theta(W/r)` and `h=Theta(sqrt(r))`, each demand in
(6.1) is `O(W/sqrt(r))`, whereas every rank in (5.1) has `Theta(W)`
available targets.  Hence there is no rank-count obstruction, but rank
counts do not prove the required conflict-free module selection.

The exact strengthened bridge target is therefore:

> Select the Catalan-scale owner-disjoint overlapping-core bridge bank with
> mutually disjoint natural suffix decks, and construct the protected trace
> factor on the complementary owners and targets with the prescribed rail
> endpoints.

This note proves neither that correlated selection nor an all-dimensional
word bound.
