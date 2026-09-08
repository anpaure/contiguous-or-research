# Lane K cross-audit: phase fusion after the RP_A retraction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

Audited source:
`MATH_ATTACK_W_PBBS_QUOTIENT_CYCLE_PHASE_FUSION_20260725.md`.

## 0. Verdict

Section 23 of `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` and
`PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md` establish that

\[
 d(D)=1
 \not\Longrightarrow
 \text{a return at gap }2\operatorname{ht}(D)+1.
\]

Consequently \((RP_A)\) is neither proved nor disproved.  Every statement
in the audited source which assumes an “updated falsity”, “exact
counterexample”, or “failure” of \((RP_A)\) is retracted.

**Pass after one material overlap correction.**  The common-carrier
suffix has length \(\delta(D_s)+|S_s|\).  Hence its literal overlap
parameter satisfies

\[
 \kappa=\Lambda+|S_s|+1,
\]

not \(\kappa=\Lambda+1\).  The phase-fusion report's \(\Lambda=0\)
sector is therefore generally larger than the one-bit \(\kappa=1\)
sector.  This correction does not damage the \(\Lambda=0\) enumeration
or its independent \(o(W)\) repair; it only narrows the claimed
dictionary between the two reports.

The mathematical constructions in that source separate cleanly from this
documentary error.  They are all stated for an **actual genuine
zero-winding return**, or as explicit conditional compilers.  With that
hypothesis retained, the following results survive unchanged:

1. the unit-deficit phase rotor at the initial edge of a genuine
   zero-winding return;
2. the two-core circular packet word of length (2s+3), and its linear
   opening of length (3s+2);
3. the exact all-phase port splice and the chain ledger
   (r(2s+3)+c(s-1));
4. the (Nq) lower bound against a separately appended all-phase chart;
5. the conditional baseline-relative quotient-cluster compiler and its
   (W+o(W)) accounting;
6. the exact enumeration and independent (o(W)) repair of the
   zero-endpoint-overlap sector.

What does **not** survive is any assertion that a dense packet sector is
known to exist, that the ordered-border compiler is forced by a disproof of
\((RP_A)\), or that the unresolved packets constitute a certified
counterexample family.  Global fusion remains a conditional fallback.

## 1. Exact translation between the two overlap parameters

For a genuine zero-winding return of step-two duration (s), use the
canonical endpoint quantities

\[
 e_0=\delta(D_0),\qquad e_s=\delta(D_s),
 \qquad N=2m+1.
\]

The common-carrier theorem in
`MATH_ATTACK_K_ZERO_WINDING_TRACE_COMPLETION_OBSTRUCTION_20260725.md`
places the forward and dual endpoint certificates in a word of length

\[
 N-2=2m-1.
\]

The prefix certificate has length \(e_0\), but the suffix certificate is

\[
 (0S_s)(0S_{s-1})\cdots(0S_1),
\]

and has length \(e_s+|S_s|\), not merely \(e_s\).  Its overlap length is
therefore

\[
 \kappa=e_0+e_s+|S_s|-(2m-1).
 \tag{1.1}
\]

The phase-fusion report defines

\[
 \Lambda=e_0+e_s-2m.
 \tag{1.2}
\]

Direct subtraction gives the exact dictionary

\[
 \boxed{\kappa=\Lambda+|S_s|+1.}
 \tag{1.3}
\]

The mandatory-overlap theorem alone gives only

\[
 \Lambda+|S_s|\ge0.
\]

Independently, the exact endpoint equations used in the phase-fusion
report give \(\Lambda\ge0\).  Consequently (1.3) gives only the one-way
implication

\[
 \boxed{\kappa=1\Longrightarrow
        \Lambda=0\text{ and }S_s=\varnothing.}
 \tag{1.4}
\]

In the other direction,

\[
 \boxed{\Lambda=0\Longrightarrow\kappa=|S_s|+1.}
 \tag{1.5}
\]

Thus the phase-fusion report's \(\Lambda=0\) chamber is the sector with no
endpoint overlap **beyond the mandatory terminal block** \(0S_s\); it is
generally larger than the one-bit common-carrier sector \(\kappa=1\).
The two notions coincide only when \(S_s\) is empty.

In particular, the symmetric capped family in the trace-completion report
has \(S_s=\varnothing\) and \(\kappa=1\), so it lies inside the
phase-fusion report's \(\Lambda=0\) chamber.  The two reports
are consistent: the first proves that this chamber has
(Omega(B_m/N)) actual starts on infinitely many ranks, while the second
proves that all of its physical phase decks can nevertheless be repaired
with (o(W)) total literal cost.  Start mass is not interval packing or
literal repair cost.

## 2. The packet compilers do not use the false converse

Let

\[
 D_h=P_h1R_h0S_h,qquad 0\le h\le s,
\]

be the actual canonical chronology of a genuine zero-winding return.  The
strict first-passage theorem gives (d(D_0)=1), but only *after* the return
has been assumed.  The phase action on a physical lift is therefore the
literal rotor

\[
 u\longmapsto u-1\pmod N.
\]

The two fixed-core owner rows of the genuine return then give the circular
packet word of length (2s+3).  Duplicating its ordered opening port of
length (s-1) gives the linear length

\[
 (2s+3)+(s-1)=3s+2.
\]

No step of this construction declares a root to be a return from the
condition (d(D)=1).  It is therefore unaffected by the sector
retraction.

Likewise, if (r) genuine packets of equal height have been supplied and
their ordered ports really match in (c) lifted chains, the exact length

\[
 \boxed{r(2s+3)+c(s-1)}
 \tag{2.1}
\]

is conditional only on literal port equality.  Relative to the
(r(2s+2)) packet-owner baseline, its excess is

\[
 \boxed{r+c(s-1).}
 \tag{2.2}
\]

These are valid compiler identities.  They do not prove that a
Catalan-dense compatible packet family exists.

## 3. The baseline-relative block implication survives

Fix (H\ll b) with (b\log N=o(m)).  Suppose every quotient block of
length (ell\in[b,2b)), together with all (N) phase lifts and its
radius-(H) collars, has a literal compiler of length

\[
 N\ell+\eta_mN\ell+C_ANH,
 \qquad \eta_m=o(1).
 \tag{3.1}
\]

There are at most (B_m/b) long-cycle blocks, while the short-cycle edge
mass is (exp(o(m))).  Summing (3.1) therefore gives

\[
 \boxed{
 W+O(\eta_mW)+O_A(WH/b)+o(W)=W+o(W).
 }
 \tag{3.2}
\]

This implication is independent of any residence lower bound.  Its
premise is unproved, so it remains a global-fusion fallback rather than a
forced conclusion.

The (Nq) lower bound for a standalone all-phase chart also survives.  It
is an architecture statement: at one rotationally rigid cut and one
depth, endpoint injectivity forces at least (Nq) equal-rank positions.
It rules out an appended (O(N+H)) seam, not coefficient one and not
residence sparsity.

## 4. The zero-excess endpoint-overlap sector is genuinely harmless

Let (e_{m,s}) count all genuine first zero-winding starts with duration
\(s\) and \(\Lambda=0\).  This class contains, but need not equal, the
\(\kappa=1\) class.  The exact kernel, Fourier
anti-concentration, and killed-path estimates in the audited source give

\[
 e_{m,s}\le C_*\frac{4^m}{s^6},
 \tag{4.1}
\]

and, uniformly in every cutoff \(H\),

\[
 \sum_{2\le s<H}e_{m,s}
 =O\!\left(\frac{4^m}{m^{5/2}}\right),
 \tag{4.2}
\]

\[
 \sum_{2\le s<H}(3s+2)e_{m,s}
 =O\!\left(\frac{4^m}{m^2}\right).
 \tag{4.3}
\]

Paying the (3s+2) packet word separately for all (N) phase lifts
therefore costs

\[
 O\!\left(
 N\frac{4^m}{m^2}
 \right)
 =O\!\left(\frac{W}{\sqrt m}\right)
 =o(W).
 \tag{4.4}
\]

Alternatively, one safe cut and one dominance chart per quotient start
costs (o_A(W)) by (4.2).  Packet overlap can only deduplicate this bill.

Thus the actual conclusion is

\[
 \boxed{
 \text{all }\Lambda=0\text{ zero-winding packets are
 independently }o(W)\text{-repairable}.}
 \tag{4.5}
\]

It is incorrect to append “therefore the counterexample to (RP_A) must
lie elsewhere”, because no counterexample is known.  The valid conditional
form is: if a dense obstruction to the linear-seam route exists, it cannot
be certified solely by the (Lambda=0\) sector.

## 5. Correct surviving boundary

After the retraction and the audited \(\Lambda=0\) repair, the exact
logical boundary is:

1. (RP_A) remains open.
2. Genuine zero-winding Gaussian starts have vanishing Catalan density.
   The independently audited intermediate-phase three-strip chart sharpens
   this to the critical bound (O_A(B_m/H)), but no
   (o_A(B_m/H)) estimate follows: its ambient capacity has matching
   order on every fixed Gaussian height band.
3. The (Lambda=0) subclass is independently (o(W))-repairable.  It
   contains the (kappa=1) subclass, whose actual start mass is
   (Omega(B_m/N)) on a subsequence; the two subclasses coincide only
   when the terminal suffix (S_s) is empty.
4. Any still-dangerous zero-winding sector must have positive endpoint
   overlap (Lambda>0) and must be controlled by actual trace clustering,
   ordered-border matching, or a baseline-relative block compiler.
5. Positive winding is a separate critical branch.
6. None of these facts forces global fusion; the compiler theorems merely
   show that fusion would compose with the correct coefficient if their
   literal matching hypotheses were proved.

This report retracts the phase-fusion source's false documentary premise
while preserving every theorem whose hypotheses explicitly begin with an
actual return or an explicit compiler.
