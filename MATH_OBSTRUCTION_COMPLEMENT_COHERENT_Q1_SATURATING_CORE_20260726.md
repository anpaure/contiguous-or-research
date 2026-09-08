# Complement-coherent \(q=1\) saturating cores: run balance, half-turn sufficiency, and the Mersenne obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

Work on the even ground

\[
 \Omega=[2m],\qquad
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1}=W-\frac{W}{m+1}.
\tag{0.1}
\]

A two-level saturating cycle between ranks \(m-1,m\) has exactly \(N\)
selected middle owners and projects to a Johnson owner cycle with every
lower intersection color exactly once.

There are three exact conclusions.

1. If its selected owner set is complement-invariant, then every
   coordinate has exactly

   \[
   \boxed{\frac{N}{2m}=\frac{\operatorname{Cat}_m}{2}}
\tag{0.2}
   \]

   one-runs along the lower-layer Hamilton cycle underlying the
   saturation.
2. Consequently no such complement-invariant selected core exists when

   \[
                         m=2^a-1.
\tag{0.3}
   \]

   These are exactly the dimensions in which \(N\), equivalently
   \(\operatorname{Cat}_m\), is odd.
3. If the projected owner cycle is itself invariant under complement,
   then complementation acts as a half-turn and the cycle is automatically
   exactly two-sided rainbow:

   \[
   X_{i+N/2}=X_i^c,
   \qquad
   \{X_i\cap X_{i+1}\}=\binom{\Omega}{m-1},
   \qquad
   \{X_i\cup X_{i+1}\}=\binom{\Omega}{m+1}.
\tag{0.4}
   \]

Thus there is no all-\(m\) exact construction of the requested kind from
one projected saturating core.  On non-Mersenne dimensions the parity and
point-run obstructions disappear, but existence remains a genuine
double-rainbow Hamilton-cycle problem.  Ordinary GMM saturation and its
cycle switches do not prove it.

The Mersenne obstruction is exact rather than asymptotic: allowing one or
more owner/color exceptions can remove its parity force.  It therefore
rules out the exact complement-invariant core uniformly in \(m\), but does
not by itself rule out an \(o(W)\)-defect complement-coherent factor.

## 1. Exact normal form of the projected saturating cycle

Write the two-level saturating cycle as

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0,
\tag{1.1}
\]

where the \(R_i\)'s are all rank-\((m-1)\) sets, the \(X_i\)'s are
distinct rank-\(m\) sets, and

\[
                         R_i\subset X_i\supset R_{i+1}.
\tag{1.2}
\]

It follows that

\[
                         X_i=R_i\cup R_{i+1}.
\tag{1.3}
\]

Hence

\[
                         R_0R_1\cdots R_{N-1}R_0
\tag{1.4}
\]

is a Hamilton cycle in \(J(2m,m-1)\) whose edge-union colors \(X_i\)
are pairwise distinct.  The projected owner cycle

\[
                         P=X_0X_1\cdots X_{N-1}X_0
\tag{1.5}
\]

has lower colors

\[
                         X_{i-1}\cap X_i=R_i,
\tag{1.6}
\]

so every lower target occurs exactly once.

Its upper colors are

\[
 \boxed{
 U_i=X_{i-1}\cup X_i
 =R_{i-1}\cup R_i\cup R_{i+1}.}
\tag{1.7}
\]

Consequently the exact upper collision excess and hole count are

\[
 c_+(P)
 :=N-\left|\{U_i:i\in\mathbb Z_N\}\right|,
\tag{1.8}
\]

\[
 \boxed{
 \#\{\text{missing upper targets}\}=c_+(P).}
\tag{1.9}
\]

The desired near-two-sided conclusion is precisely \(c_+(P)=o(W)\).

## 2. Complement-invariant owner support forces exact run balance

Let

\[
                         V(P)=\{X_0,\ldots,X_{N-1}\}.
\tag{2.1}
\]

Fix a coordinate \(x\in\Omega\), and write

\[
                         \epsilon_i=\mathbf 1_{\{x\in R_i\}}.
\tag{2.2}
\]

Put

\[
 d_x=|\{i:x\in R_i\}|
 =\binom{2m-1}{m-2}
 =\frac{m-1}{2m}N,
\tag{2.3}
\]

and let \(\rho_x\) be the number of cyclic one-runs in
\((\epsilon_i)_{i\in\mathbb Z_N}\).

### Theorem 2.1 (point-run identity)

For every coordinate \(x\),

\[
 |\{i:x\in X_i\}|=d_x+\rho_x.
\tag{2.4}
\]

If \(V(P)\) is complement-invariant, then

\[
 \boxed{\rho_x=\frac{N}{2m}
 =\frac{\operatorname{Cat}_m}{2}}
\qquad(x\in\Omega).
\tag{2.5}
\]

#### Proof

By (1.3), \(x\in X_i\) exactly when

\[
                         \epsilon_i\vee\epsilon_{i+1}=1.
\]

In a nonconstant cyclic binary word, the number of adjacent pairs with at
least one \(1\) is the number of \(1\)-positions plus the number of
\(0\to1\) transitions.  The latter is the number \(\rho_x\) of one-runs,
proving (2.4).

If \(V(P)\) is complement-invariant, its owners occur in complement pairs.
Exactly one owner in each pair contains \(x\), so

\[
                         |\{i:x\in X_i\}|=N/2.
\]

Subtract (2.3) from this equality:

\[
 \rho_x
 =\frac N2-\frac{m-1}{2m}N
 =\frac{N}{2m}.
\]

Finally,

\[
 \frac{N}{2m}
 =\frac{1}{2(m+1)}\binom{2m}{m}
 =\frac{\operatorname{Cat}_m}{2}.
\]

This proves (2.5). \(\square\)

Thus complement invariance is much stronger than a cardinality condition:
all \(2m\) coordinate words on the lower Hamilton cycle must have the
same exact run count.

More generally, complement invariance gives the hierarchy

\[
 |\{X\in V(P):S\subseteq X\}|
 =
 |\{X\in V(P):X\cap S=\varnothing\}|
\tag{2.6}
\]

for every \(S\subseteq\Omega\).  Equation (2.5) is its singleton
projection.

## 3. The exact Mersenne obstruction

### Theorem 3.1 (infinite parity obstruction)

A complement-invariant selected owner set for the exact saturating core
can exist only if \(\operatorname{Cat}_m\) is even.  Equivalently, it is
ruled out by parity whenever

\[
                         m=2^a-1,
\tag{3.1}
\]

and these are exactly the dimensions in which the parity condition fails.

#### Proof

Complementation has no fixed rank-\(m\) owner, so every
complement-invariant owner family has even cardinality.  By (0.1), the
core has cardinality \(N\), and (2.5) also requires
\(\operatorname{Cat}_m/2\) to be integral.

The Catalan number \(\operatorname{Cat}_m\) is odd exactly for
\(m=2^a-1\).  One direct verification uses Kummer's theorem:

\[
 N=\binom{2m}{m-1}
\]

is odd exactly when adding \(m-1\) and \(m+1\) in base two creates no
carry.  If \(m\) is even, their terminal \(1\)-bits already create a
carry.  If \(m\) is odd, write its terminal block of ones as
\(m=p\,0\,1^t\).  The high prefix \(p\) occurs in both \(m-1\) and
\(m+1\), so carry-freeness forces \(p=0\), i.e. \(m=2^t-1\).
Conversely those Mersenne values are plainly carry-free. \(\square\)

No sequence of cycle switches which preserves the exact \(N\)-owner
saturating core can overcome this obstruction in the Mersenne dimensions.

## 4. Half-turn complement symmetry would solve both colors exactly

If only \(V(P)\) is complement-invariant, then the complemented cycle
\(\overline P\) is an upper-perfect Johnson cycle on the same owner set:

\[
 V(\overline P)=V(P),\qquad
 U(\overline P)=
 \{R^c:R\in\binom{\Omega}{m-1}\}.
\tag{4.0}
\]

This gives two Hamilton cycles on the same support, one lower-perfect and
one upper-perfect.  It gives no common-edge or common-order estimate, so
overlaying them is not itself a two-sided cycle.

Suppose the projected owner cycle \(P\), not merely its vertex set, is
invariant under complementation as an unoriented cycle.

### Theorem 4.1 (half-turn theorem)

For \(m\ge2\), \(N\) must be even and, after a cyclic reindexing,

\[
                         X_{i+N/2}=X_i^c.
\tag{4.1}
\]

Moreover \(P\) is exactly upper-rainbow whenever it is exactly
lower-rainbow.

#### Proof

Complementation induces a fixed-point-free involutive automorphism of the
abstract cycle \(C_N\).  An involutive cycle automorphism is a half-turn
or a reflection.

A reflection through vertices would fix a middle owner, impossible.  A
reflection through edges would fix an unordered Johnson edge.  Its two
endpoints would then have to be complements, but complementary \(m\)-sets
have Johnson distance \(m>1\).  Thus reflection is impossible, leaving
only the half-turn (4.1).

For every owner edge,

\[
 (X_i\cap X_{i+1})^c
 =X_i^c\cup X_{i+1}^c.
\tag{4.2}
\]

The half-turn permutes the edge set.  Hence complementation bijects the
lower color multiset of \(P\) to its upper color multiset.  Since all
rank-\((m-1)\) lower colors occur exactly once, all rank-\((m+1)\)
upper colors do also. \(\square\)

In directed form, if

\[
                         X_{i+1}=X_i-a_i+b_i,
\]

then the half-turn obeys

\[
                         a_{i+N/2}=b_i,\qquad
                         b_{i+N/2}=a_i.
\tag{4.3}
\]

This is the exact complement-coherent \(q=1\) target.  It is sufficient,
but stronger than the user's requirement that only \(V(P)\) be
complement-invariant.

## 5. What bounded cycle switching can and cannot change

It is useful to state the switch ledger independently of any particular
GMM recursion.

Take the lower Hamilton cycle (1.4).  A legal two-edge switch removes two
cycle edges and inserts the opposite pair so that one Hamilton cycle
remains and all new edge-union colors are distinct.  It therefore remains
a projected saturating cycle.

Define the support defect

\[
 \delta_c(P)=\frac12|V(P)\mathbin\triangle V(P)^c|.
\tag{5.1}
\]

### Proposition 5.1 (local-switch Lipschitz bounds)

One two-edge switch changes

\[
                         \delta_c(P)
\quad\text{and}\quad c_+(P)
\]

by at most \(4\) each.

#### Proof

The switch replaces two lower-cycle edges by two others.  Since their edge
unions are the selected owners, at most two old owners disappear and at
most two new owners appear.  Thus

\[
                         |V(P)\triangle V(P')|\le4.
\]

The same holds after complementation, and the triangle inequality for
symmetric difference gives
\(|\delta_c(P)-\delta_c(P')|\le4\).

For the upper colors, use (1.7).  A two-edge switch reverses at most one
cyclic segment.  At every vertex strictly inside that segment, the two
neighbors merely exchange order, so the triple union in (1.7) is
unchanged.  Only the at most four vertices incident with the switched
edges can acquire a new triple union.  Replacing four occurrence values
changes the support size, hence \(c_+\), by at most four. \(\square\)

Consequently any construction starting from a cycle \(P_0\) and using
\(s\) such local switches satisfies

\[
 s\ge\frac14\delta_c(P_0)
\tag{5.2}
\]

before its selected support can become complement-invariant, and

\[
 s\ge\frac14\bigl(c_+(P_0)-o(W)\bigr)
\tag{5.3}
\]

before its upper holes become \(o(W)\).

The GMM saturating-cycle theorem supplies no estimate for either starting
quantity.  Thus local switchability of the saturating-cycle space is not
an expansion theorem for the two required statistics.  In particular, a
proof that the switch graph is connected would still be insufficient
without a route whose cumulative defect descent is controlled.

A family of switches preserves complement invariance at every intermediate
stage only when the signed multiset of removed and inserted edge-union
colors is complement-closed.  Because complementation sends a lower
rank-\((m-1)\) cycle vertex to rank \(m+1\), the required mate is not a
local switch on the same lower cycle; it is a nonlocal paired trade.

## 6. Exact surviving problem

For \(m\not=2^a-1\), no scalar obstruction found here excludes a
complement-invariant selected support.  The exact remaining construction is
a Hamilton cycle \(R_0,\ldots,R_{N-1}\) in \(J(2m,m-1)\) such that:

1. its edge unions \(X_i=R_i\cup R_{i+1}\) are distinct;
2. \(\{X_i\}\) is complement-invariant, equivalently it satisfies the
   full hierarchy (2.6);
3. the triple-union map

   \[
   i\longmapsto R_{i-1}\cup R_i\cup R_{i+1}
\tag{6.1}
   \]

   has image size \(N-o(W)\).

The stronger half-turn condition (4.1) would replace item 3 by exact upper
rainbowness.

This is not supplied by GMM Corollary 2.  It is also not implied by the
known existence of a \(W-o(W)\)-edge two-sided-rainbow Johnson linear
forest: converting such a forest into one owner cycle has additional
endpoint Hall cuts.

The decisive current conclusion is therefore mixed:

* **exact obstruction:** the requested exact complement-invariant
  saturating core is impossible for every Mersenne \(m=2^a-1\);
* **exact sufficient construction:** a half-turn complement-invariant
  projected core would solve both \(q=1\) ledgers perfectly; and
* **open non-Mersenne gate:** build the run-balanced cycle in Section 6
  or prove a further invariant of its paired switch space.
