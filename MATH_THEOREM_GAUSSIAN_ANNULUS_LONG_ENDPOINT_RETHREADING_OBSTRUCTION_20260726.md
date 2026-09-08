# Gaussian annulus reuse forces positive-density long endpoint rethreading

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed, and let \(h=o(\sqrt m)\).  The unconditional
PBBS word already covers the paired band through depth \(h\) in
\(W+o(W)\) letters.  This note asks whether the same baseline can cover
the Gaussian annulus

\[
h<q\le H
\tag{0.2}
\]

without paying a second \(W\)-scale word.

The two audited inputs have exactly this mismatch.  With
\(B=W/(2m+1)=\operatorname{Cat}_m\), the PBBS length is

\[
 L_{\rm PBBS}(h)=W+O(Bh\sqrt m)=W+o(W),
\tag{0.2a}
\]

whereas the normalized odd product-SCD tail at cutoff
\(H/\sqrt m\to A\) tends to the strictly positive constant

\[
 F(A)=2\sqrt2\int_0^\infty
 8\sqrt{2/\pi}\,y^2e^{-2y^2}e^{-2(A-y)_+^2}\,dy.
\tag{0.2b}
\]

That tail is \(o(W)\) exactly when \(H/\sqrt m\to\infty\).  Thus any
fixed-Gaussian bridge must reuse or replace baseline positions rather
than append the established tail.

There is an exact obstruction to every small witness-preserving surgery.
Let \(Z\) be any nonzero literal word of length

\[
 |Z|=W+e,
 \qquad e=o(W),
\tag{0.3}
\]

which represents every rank-\(m\) set and every rank-\((m-q)\) set for
all \(h<q\le H\).  Choose one witness interval for every represented
set.  Then there are constants \(c_A,c'_A>0\) such that at least

\[
 \boxed{c_AW}
\tag{0.4}
\]

of the rank-\(m\) witness intervals have length at least

\[
 \boxed{c'_A\sqrt m.}
\tag{0.5}
\]

The complementary statement holds for the upper annulus: if all
rank-\((m+1+q)\) sets are represented, then a positive fraction of the
rank-\((m+1)\) witness intervals have Gaussian length, with the flag
threaded from their right endpoints.

More generally, if all but \(r\) chosen middle-owner witnesses have
length at most \(g\), where \(g=o(\sqrt m)\), then

\[
 \boxed{r\ge c_AW.}
\tag{0.6}
\]

The designated owner witnesses in the depth-\(h\) PBBS erosion baseline
have length \(h+1=o(\sqrt m)\), apart from the already charged
\(o(W)\) seam neighborhoods.  Therefore a Gaussian-annulus compiler
cannot preserve those witnesses outside \(o(W)\) exceptions.  It must
globally rethread a positive density of lower left-endpoint intervals and,
independently, a positive density of upper right-endpoint intervals.

This is stronger than the previous append-only and independent-collar
no-go statements.  It applies to an arbitrary final word and arbitrary
helper letters; its only architecture-local conclusion is the last one,
where the short PBBS witnesses are assumed retained.

The obstruction is not a universal impossibility theorem.  A Boolean SCD
gives an exact static allocation of every annular target into nested flags
ending at middle owners, with no Hall deficit.  Hence the surviving gate
is literal chronology: realize positive-density Gaussian-length flags on
both endpoint skeletons in one near-\(W\) word.  No such PBBS braid is
constructed here.

## 1. Exact endpoint incidence

The following lemma is independent of PBBS.

### Lemma 1.1 (annular common-start ledger)

Let a nonzero word of length

\[
 L=M+e
\tag{1.1}
\]

represent \(M\) distinct targets of one rank.  At each depth
\(q\in Q\), let it also represent \(D_q\) distinct targets of a smaller
rank.  Choose one witness for every target.  For each selected witness of
the mandatory rank, write \(p\) for its left endpoint and let \(a_p\) be
the number of depths \(q\in Q\) at which a selected lower target shares
that endpoint.

Then

\[
 \boxed{
 R:=\sum_pa_p
 \ge\sum_{q\in Q}(D_q-e)_+.}
\tag{1.2}
\]

If \(t=|Q|\), and

\[
 N_d=|\{p:a_p\ge d\}|,
\tag{1.3}
\]

then, for every \(1\le d\le t\),

\[
 \boxed{
 N_d\ge
 \max\left\{0,
 {R-M(d-1)\over t-d+1}
 \right\}.}
\tag{1.4}
\]

Every mandatory witness counted by \(N_d\) has at least \(d\) word
positions.

#### Proof

Distinct equal-rank target witnesses have distinct left endpoints.  If
two intervals had the same left endpoint, they would be nested, so their
ORs would be comparable; distinct sets of the same rank are incomparable.
Thus the mandatory starts form an \(M\)-subset of the \(L=M+e\)
positions, while the depth-\(q\) starts form a \(D_q\)-subset.  Their
intersection has size at least

\[
 M+D_q-L=D_q-e.
\tag{1.5}
\]

At a common start, the smaller-rank witness ends strictly before the
mandatory witness.  For one fixed start, witnesses at different ranks
have distinct right endpoints.  Summing (1.5) over the depths proves
(1.2).

Since \(0\le a_p\le t\),

\[
 R\le N_dt+(M-N_d)(d-1).
\tag{1.6}
\]

Rearranging proves (1.4).  Finally, \(d\) distinct lower-rank right
endpoints occur strictly before the mandatory right endpoint, so the
mandatory interval contains at least \(d+1\) positions; the weaker
stated bound follows. \(\square\)

The right-endpoint version is obtained by reversing the word.  There a
larger-rank target sharing a mandatory right endpoint begins strictly
before it, and the same ledger applies.

## 2. Exact Gaussian rank census

For \(0\le q\le H\), put

\[
 N_q=\binom{2m+1}{m-q}
     =\binom{2m+1}{m+1+q}.
\tag{2.1}
\]

The exact ratio is

\[
 \boxed{
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+2+j}.}
\tag{2.2}
\]

Uniformly for \(q\le A\sqrt m+O(1)\), Taylor expansion of the logarithm
gives

\[
 \log{N_q\over W}
 =-{q(q+1)\over m}+O_A(m^{-1/2}).
\tag{2.3}
\]

In particular, with

\[
 \rho_A={1\over2}e^{-A^2},
\tag{2.4}
\]

one has, for all sufficiently large \(m\),

\[
 \boxed{N_q\ge\rho_AW\qquad(0\le q\le H).}
\tag{2.5}
\]

Nothing probabilistic enters (2.3): expand each factor of (2.2), noting
that the total cubic remainder is
\(O(q^3/m^2)=O_A(m^{-1/2})\).

## 3. Positive-density Gaussian flags are necessary

Let

\[
 Q=\{h+1,h+2,\ldots,H\},
 \qquad t=H-h.
\tag{3.1}
\]

Since \(h=o(\sqrt m)\),

\[
 t=(A+o(1))\sqrt m.
\tag{3.2}
\]

### Theorem 3.1 (long left-endpoint rethreading)

Assume (0.3), and assume that \(Z\) represents every rank-\(m\) set and
all lower annulus ranks \(m-q\), \(q\in Q\).  Then, for all sufficiently
large \(m\), at least

\[
 {\rho_A\over8}W
\tag{3.3}
\]

chosen rank-\(m\) witnesses have length at least

\[
 {\rho_A\over3}t.
\tag{3.4}
\]

#### Proof

Apply Lemma 1.1 with \(M=W\) and \(D_q=N_q\).  By (2.5),

\[
 R\ge\sum_{q\in Q}(N_q-e)_+
 \ge t(\rho_AW-e)
\tag{3.5}
\]

for all large \(m\), because \(e/W\to0\).  We may assume

\[
 e\le {\rho_A\over8}W.
\tag{3.6}
\]

Take

\[
 d=\left\lfloor{\rho_A t\over2}\right\rfloor.
\tag{3.7}
\]

For large \(m\), \(d\ge\rho_At/3\).  Equations (1.4)--(3.7) give

\[
 \begin{aligned}
 N_d
 &\ge {t(\rho_AW-e)-W(d-1)\over t-d+1}\\
 &\ge { (3\rho_A/8)tW\over t+1}
 \ge {\rho_A\over8}W.
 \end{aligned}
\tag{3.8}
\]

Here the second line uses
\(R\ge(7\rho_A/8)tW\),
\(W(d-1)\le(\rho_A/2)tW\), and
\(t/(t+1)\ge1/2\).  Every witness counted by \(N_d\) has length at least
\(d\), proving
(3.3)--(3.4). \(\square\)

### Corollary 3.2 (short-witness obstruction)

Under the hypotheses of Theorem 3.1, suppose all but \(r\) of the chosen
rank-\(m\) witnesses have length at most \(g=g(m)\), where

\[
 g=o(\sqrt m).
\tag{3.10}
\]

Then, for all sufficiently large \(m\),

\[
 \boxed{r\ge{\rho_A\over8}W.}
\tag{3.11}
\]

#### Proof

By (3.2)--(3.4), eventually \((\rho_A/3)t>g\).  Hence every witness
counted in (3.3) belongs to the exceptional family. \(\square\)

### Theorem 3.3 (upper right-endpoint rethreading)

Assume that \(Z\) represents every rank-\((m+1)\) set and every upper
annulus rank \(m+1+q\), \(q\in Q\).  Then (3.3)--(3.4) hold for chosen
rank-\((m+1)\) witnesses, with flags sharing their right endpoints.

#### Proof

Apply the right-endpoint version of Lemma 1.1 with mandatory rank
\(m+1\), larger annular ranks \(m+1+q\), and the same census (2.1).
The proof of Theorem 3.1 is otherwise unchanged.
\(\square\)

The lower and upper exceptional families need not be disjoint.  The
theorem asserts two simultaneous endpoint requirements, not
\((\rho_A/4)W\) distinct middle objects.

## 4. Consequence for the proved sub-Gaussian PBBS baseline

Run the unconditional PBBS compiler with parameter \(h+1\).  Away from
its cut neighborhoods, its designated middle-owner witness has the
endpoint-capped erosion form

\[
 X_i=\bigcup_{p=i-h-1}^{i}D_p,
\tag{4.1}
\]

up to the harmless one-index convention of the compiler.  Thus every
designated owner witness has \(h+O(1)=o(\sqrt m)\) positions.

The total size of the cut neighborhoods is bounded by the same
collar-times-cut ledger that occurs in the word-length estimate.  At a
sub-Gaussian cutoff it is \(o(W)\).  Hence all but \(o(W)\) middle owners
come with designated shallow witnesses of length \(o(\sqrt m)\).

### Corollary 4.1 (no exceptional-set annulus patch)

No word satisfying the Gaussian annulus conclusions can retain the
designated shallow PBBS owner witnesses for all but \(o(W)\) rank-\(m\)
owners.  The analogous statement holds for the upper central owners and
their right-endpoint witnesses.

#### Proof

Apply Corollary 3.2 with \(g=h+O(1)\).  The permitted exceptional family
must have size at least \((\rho_A/8)W\), contradicting \(o(W)\).
The upper assertion is Theorem 3.3. \(\square\)

This conclusion permits changing every word letter and choosing entirely
new witnesses.  What it forbids is calling the result a local patch of
the old baseline while retaining almost all of its designated short
owner intervals.  A successful construction must rethread a positive
density of those intervals to Gaussian span.  This remains compatible
with total length \(W+o(W)\), because long witness intervals can overlap
heavily.

## 5. Static owner allocation has no Hall obstruction

The preceding theorem is chronological, not a source-capacity deficit.

### Proposition 5.1 (exact SCD annulus flags)

Fix any symmetric chain decomposition of \(2^{[2m+1]}\).  Assign every
lower target \(T\), \(|T|=m-q\), to the unique rank-\(m\) member of its
SCD chain.  Assign every upper target \(U\), \(|U|=m+1+q\), to the unique
rank-\((m+1)\) member of its chain.  Then:

1. every annular target is assigned exactly once;
2. each middle owner receives at most one target at each rank; and
3. all targets assigned to one owner are nested in the required rank
   order.

#### Proof

A symmetric chain beginning at rank \(a\) ends at rank
\(2m+1-a\).  If it contains a set of rank at most \(m\), then it passes
through rank \(m\) and rank \(m+1\); the same holds in reverse for a set
of rank at least \(m+1\).  A chain contains at most one member of each
rank.  Since the SCD partitions the Boolean lattice, all three assertions
follow. \(\square\)

Thus the exact rank marginals and nested-owner flags can be satisfied
integrally and simultaneously through every depth.  What Proposition 5.1
does not supply is a common literal ordering of their interval endpoints.
In particular it does not show that the lower left-endpoint flags and the
upper right-endpoint flags can coexist with the PBBS owner chronology in
one word.

## 6. Exact remaining Gaussian-annulus gate

The proved and obstructed architectures now separate cleanly.

* Appending an independent annulus or exterior word at fixed
  \(A\sqrt m\) costs \(\Omega_A(W)\) by the boundary antichain.
* Protected erosion deletion, independent collar replacement, and the
  additive clustered seam all retain an \(\Omega_A(W)\) critical bill.
* Corollary 4.1 now rules out a non-additive patch which nevertheless
  preserves the shallow PBBS witness geometry outside \(o(W)\) owners.
* Proposition 5.1 rules out a static Hall explanation for the failure:
  the annular targets do admit exact integral nested owner allocation.

Therefore the literal missing theorem is the following positive-density
rethreading statement.

> **Gaussian PBBS annulus braid — open.**  Replace the designated
> sub-Gaussian PBBS owner intervals on a positive density of both central
> antichains by intervals of length \(\Theta_A(\sqrt m)\), while keeping
> the total word length \(W+o_A(W)\), and order their internal increments
> so that:
>
> 1. every lower annulus target is carried by a common-left-endpoint
>    nested flag;
> 2. every upper annulus target is carried by a common-right-endpoint
>    nested flag;
> 3. the already proved depths \(q\le h\) retain some correct witnesses,
>    not necessarily their old canonical witnesses; and
> 4. all PBBS crossing targets and both central antichains remain exactly
>    owned.

Theorems 3.1 and 3.3 show that the positive density and Gaussian span in
this gate are necessary, not aesthetic choices.  Proposition 5.1 shows
that only the literal endpoint chronology, rather than target supply,
remains unresolved.

## 7. Status

Proved here:

1. the exact common-start incidence ledger (1.2)--(1.4);
2. the Gaussian rank lower bound (2.5);
3. positive-density Gaussian-span lower and upper endpoint flags;
4. the obstruction to retaining all but \(o(W)\) designated shallow PBBS
   owner witnesses; and
5. exact integral SCD allocation of every annular target.

Not proved here:

1. a PBBS Gaussian-annulus braid;
2. a universal impossibility theorem for wholesale endpoint rethreading;
3. coefficient one for the full Boolean lattice.

The frontier has therefore moved from additive seam cost to an exact
positive-density chronology problem: a successful non-additive compiler
must make Gaussian-length witness intervals typical on both endpoint
skeletons, even though the word itself has only \(W+o(W)\) positions.

## 8. Subsequent audit: anti-dihedral rigidity and the direct rotor gate

`MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`
first shows that anti-dihedral symmetry would identify every lower trace
with the corresponding upper trace.  However, comparing one symmetric
transition proves

\[
                         s_{i+n}=s_i.
\]

Distinct middle windows then force every component to have length exactly
(n), so it is one ordinary wreath.  An anti-dihedral singleton factor has
(W/n) components and cannot satisfy the sub-Catalan component condition
needed by the direct sliding-spine linearization.  Thus reflection symmetry
is a statewise dead end for long singleton rethreading, not a positive
shortcut.

The same note isolates the surviving architecture.  A binary-rotor
fibre-transversal circulation with

* (o(W/m)) components,
* lower **and upper** prefix coverage through the required depth, and
* no anti-dihedral requirement

has a direct linearization of length

\[
 W+C(m+H)=W+o(W).
\]

Every middle witness then has length (m).  The note gives exact Boolean
circulation equations for this object and proves a common fractional point
which balances every prefix rank simultaneously.  What remains is the
correlated integral rounding with both prefix covers and few cycles.

This does not prove that the required integral rotor circulation exists.
It sharpens the chronology boundary in both directions: long singleton
witnesses would meet the incidence obstruction at density one, but the
tempting reflection mechanism which makes their two sides coherent is too
rigid to compress the wreath components.
