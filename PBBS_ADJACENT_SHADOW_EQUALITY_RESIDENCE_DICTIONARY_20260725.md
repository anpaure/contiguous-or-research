# Adjacent floor-shadow equality is exactly coordinate residence

Date: 2026-07-25

This note concerns only the coefficient-one PBBS residence gate.  It
classifies the adjacent-equality statistic suggested by the in-place
compiler audit.

## 1. A general Johnson-path identity

Let \((X_i)\) be a rank-\(k\) Johnson path and write its transition as

\[
 X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\}.
 \tag{1.1}
\]

For \(q\ge1\), put

\[
 L_{i,q}=\bigcap_{h=0}^{q}X_{i+h}.
 \tag{1.2}
\]

Call this shadow floor-correct when \(|L_{i,q}|=k-q\).

### Theorem 1.1 (adjacent-equality dictionary)

Suppose both \(L_{i,q}\) and \(L_{i+1,q}\) are floor-correct.  Then

\[
 \boxed{L_{i,q}=L_{i+1,q}
        \quad\Longleftrightarrow\quad
        \beta_i=\alpha_{i+q}.}
 \tag{1.3}
\]

In this event the common coordinate \(x=\beta_i=\alpha_{i+q}\) is
present at exactly the \(q\) consecutive owner times

\[
 i+1,i+2,\ldots,i+q
 \tag{1.4}
\]

between its displayed entry and exit.  Thus (1.3) is exactly a bounded
positive coordinate run of length \(q\).

#### Proof

Put

\[
 M=\bigcap_{h=1}^{q}X_{i+h}.
\]

This is an intersection of \(q\) consecutive rank-\(k\) Johnson owners,
so

\[
 |M|\ge k-q+1.                                      \tag{1.5}
\]

Since \(M\subseteq X_{i+1}\) and
\(X_{i+1}\setminus X_i=\{\beta_i\}\), intersecting \(M\) with
\(X_i\) deletes at most \(\beta_i\).  Hence

\[
 k-q=|L_{i,q}|=|M\cap X_i|\ge |M|-1.
\]

Together with (1.5), this forces

\[
 |M|=k-q+1,
 \qquad
 L_{i,q}=M\setminus\{\beta_i\},
 \qquad \beta_i\in M.                              \tag{1.6}
\]

The same argument at the right endpoint gives

\[
 L_{i+1,q}=M\setminus\{\alpha_{i+q}\},
 \qquad \alpha_{i+q}\in M.                         \tag{1.7}
\]

Equations (1.6)--(1.7) prove (1.3).  Membership of \(x\) in \(M\),
together with its entry and exit transitions, proves (1.4). \(\square\)

### Lemma 1.2 (a shortest run is automatically exposed)

If \(x\) has an internally bounded positive run of minimum possible
length \(q\), at owner times \(i+1,\ldots,i+q\), then both adjacent
shadows in (1.3) are floor-correct and equal.

#### Proof

Equality follows coordinatewise from the entry and exit of \(x\), as in
the identity

\[
 \bigcap_{h=0}^{q}X_{i+h}
 =\bigcap_{h=1}^{q+1}X_{i+h}.
\]

If either intersection had size larger than \(k-q\), fewer than \(q\)
of its \(q\) transitions would be first departures of coordinates present
at the initial owner.  Some arrival would therefore depart again strictly
inside the window.  That coordinate would have a positive run shorter than
\(q\), contradicting minimality. \(\square\)

## 2. Exact PBBS translation

On one complement-projected step-two parity, write

\[
 Y_j=X_{p+2j}.
\]

The audited PBBS transition recurrence is

\[
 Y_{j+1}
 =Y_j-\{\lambda_{p+2j}\}+\{\lambda_{p+2j+1}\}.
 \tag{2.1}
\]

Apply Theorem 1.1 with

\[
 \alpha_j=\lambda_{p+2j},
 \qquad
 \beta_j=\lambda_{p+2j+1}.
\]

### Corollary 2.1 (PBBS adjacent equality)

For two adjacent floor-correct depth-\(q\) PBBS shadows,

\[
 \boxed{
 L_{j,q}=L_{j+1,q}
 \quad\Longleftrightarrow\quad
 \lambda_{p+2j+1}=\lambda_{p+2j+2q}.}
 \tag{2.2}
\]

The two displayed occurrences are consecutive occurrences of that omitted
label, and their odd gap is

\[
 \boxed{2q-1.}                                      \tag{2.3}
\]

Equivalently, adjacent floor-shadow equality at depth \(q\) is precisely
an exposed projected PBBS positive residence of length \(q\).

#### Proof

Equation (2.2) is Theorem 1.1.  Its common label is present in every
intermediate owner, so it cannot have an intervening omitted-label
occurrence.  The index difference is \(2q-1\), proving (2.3). \(\square\)

Let \(C_q^{\rm fc}\) be the total number of adjacent equal pairs of
floor-correct depth-\(q\) shadows, and let \(M_s\) be the number of
consecutive PBBS omitted-label gaps \(2s+1\).  Then

\[
 \boxed{C_q^{\rm fc}\le M_{q-1}.}                  \tag{2.4}
\]

Equality holds for a gap whenever its two surrounding depth-\(q\) windows
are floor-correct; in particular it holds at the globally shortest
residence length.  The exact PBBS slope inversion gives

\[
 \boxed{M_{q-1}=E_q-2E_{q-1}+E_{q-2}.}             \tag{2.5}
\]

Thus the adjacent-equality statistic is a local presentation of the same
residence measure already appearing in the coefficient-one packing gate.

## 3. The first nontrivial depths

The PBBS has no gap-one or gap-three return.  Therefore

\[
 \boxed{C_1^{\rm fc}=C_2^{\rm fc}=0.}              \tag{3.1}
\]

At depth three, gap five is the first possible residence.  Hence every
gap-five run is shortest and Lemma 1.2 applies.  The exact gap-five
classification gives \(r-1\) normalized roots and \(N=2r+1\) spatial
phases.  Consequently

\[
 \boxed{C_3^{\rm fc}=N(r-1).}                      \tag{3.2}
\]

This is polynomial and therefore

\[
 C_3^{\rm fc}=o(B_r/\sqrt r).
\]

At depth four, every adjacent equality comes from a gap-seven return, so
the exact gap-seven census gives

\[
 \boxed{C_4^{\rm fc}
 \le N(2^{r-1}-r)=o(B_r/\sqrt r).}                 \tag{3.3}
\]

Some gap-seven windows can contain a shorter gap-five run, so equality in
(3.3) is not asserted.

## 4. Exact coefficient-one meaning

Every selected short residence interval gives one adjacent equality at
its own depth once it is shortest inside the relevant packet.  Conversely,
Theorem 1.1 reconstructs that residence interval from the equality.  Thus
an aggregate estimate

\[
 \sum_{q\le A\sqrt r}C_q^{\rm fc}
 =o_A(B_r/\sqrt r)
\]

would imply the quotient residence gate, but it is stronger than needed.
Without a new aggregate PBBS theorem, (2.4)--(2.5) merely reformulate the
existing obstruction: at growing depth, adjacent equalities are exactly
short coordinate residences.

The useful gain is therefore precise but limited:

* depth two has no adjacent equality at all;
* depths three and four are negligible by exact PBBS censuses;
* the first possible critical contribution must come from gaps tending to
  infinity with \(r\).

