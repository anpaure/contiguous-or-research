# K17 `P*` fresh tickets: exact local interface and host-mutability obstruction

**Date:** 2026-08-02  
**Status:** exact local theorem and exact finite obstruction.  This note
characterizes canonical five-cell validity under either s7 owner phase,
proves that the phase enters through exactly two owner-extension points, and
proves that changing only the short address and endpoint flags cannot repair
any failed record of the regenerated `1,748`-ticket ledger.  It does **not**
construct or refute a fresh phase-specific ticket packing, a bounded carried
connector/reset state, history closure, residence, supplier, compiler, a
selected `z=6` witness, or a word.

## 1. Frozen objects and notation

Fix the planted target table `T` and the two s7 owner maps

```text
scratch/k17_common_basis_b5_protected_host_20260802/
  constructed_common_basis_b5_host.tsv

scratch/ad_k17_s7_carrier_adapter_20260802/out/
  round047.s7.phase0.tsv
  round047.s7.phase1.tsv
```

The target row and root at every physical host are common to the two owner
phases.  Write `O_phi(v)` for the phase-`phi` owner and `R_v` for the common
root.  On all `24,310` rows in each phase,

\[
 R_v\subset O_\phi(v),\qquad
 d_\phi(v):=O_\phi(v)\setminus R_v
 \quad\hbox{is a singleton}.                              \tag{1.1}
\]

A ticket geometry is

\[
             \tau=(s,p,u;q,\alpha,\beta),                  \tag{1.2}
\]

where `s` is the short row, `p,u` are the predecessor and successor long
hosts, `q in {7,8}` is the canonical short address, and
`alpha,beta in {0,1,2,3}` are the long flags.  The reset-monotone menu has
`beta<=alpha`, hence exactly `20` possible triples `(q,alpha,beta)` on a
fixed host triple `(s,p,u)`.

For a long row `B subset M subset R`, let

\[
 (x_0,x_1,x_2)=(B,M\setminus B,R\setminus M),\qquad
 (X_0,X_1,X_2)=(B,M,R).                                    \tag{1.3}
\]

Flag `alpha` applies one of the four permutations

\[
 (012),(102),(201),(210)                                   \tag{1.4}
\]

to both triples.  Denote the resulting predecessor pairs by
`(x_i^alpha,X_i^alpha)` and the successor pairs by
`(y_i^beta,Y_i^beta)`.

For the short row `L subset U`, put

\[
\begin{array}{c|c|c|c}
q&(\lambda_0,\lambda_1,\lambda_2)&
   (\Lambda_0,\Lambda_1,\Lambda_2)&C_q\\ \hline
7&(0,0,U\setminus L)&(L,L,U)&\{0,1\}\\
8&(U\setminus L,0,0)&(U,L,L)&\{1,2\}.
\end{array}                                                 \tag{1.5}
\]

Here `C_q` gives the two short-covered members among physical cells
`1,2,3`.

## 2. Exact five-envelope predicate

For phase `phi`, define five lower and upper envelopes by

\[
\begin{array}{lll}
a_0=x_0^\alpha\cup d_\phi(s),
 &\quad&A_0=X_0^\alpha\cap O_\phi(s),\\
a_1=x_1^\alpha\cup\lambda_0\cup d_\phi(u),
 &&A_1=X_1^\alpha\cap\Lambda_0\cap O_\phi(u),\\
a_2=x_2^\alpha\cup\lambda_1\cup y_0^\beta,
 &&A_2=X_2^\alpha\cap\Lambda_1\cap Y_0^\beta,\\
a_3=\lambda_2\cup y_1^\beta,
 &&A_3=\Lambda_2\cap Y_1^\beta,\\
a_4=y_2^\beta,
 &&A_4=Y_2^\beta.
\end{array}                                                 \tag{2.1}
\]

### Theorem 2.1 (exact local ticket criterion)

The ticket geometry (1.2) has a canonical physical five-cell realization
under owner phase `phi` if and only if

\[
       \varnothing\ne A_i\quad\hbox{and}\quad a_i\subseteq A_i
                    \qquad(0\le i\le4),                    \tag{2.2}
\]

and

\[
       L\subseteq\bigcup_{j\in C_q} A_{j+1}.                \tag{2.3}
\]

Consequently the complete phase-dependent input to local validity is the
ordered pair of one-point markers

\[
                         (d_\phi(s),d_\phi(u)).              \tag{2.4}
\]

The predecessor owner and both outer token labels are absent from the
predicate.

#### Proof

Every physical cell `c_i` must satisfy
`a_i subseteq c_i subseteq A_i` and be nonempty, proving necessity of
(2.2).  The two cells indexed by `C_q` must have union `L`, proving (2.3).

Conversely begin with `c_i=a_i`.  For every point of `L` not yet present in
the two covered cells, (2.3) supplies a covered upper envelope containing
that point; add it there.  Fill any still-empty cell by one arbitrary point
of its nonempty upper envelope.  Covered upper envelopes lie in `L`, all
three middle upper envelopes lie in `U`, and the unique uncovered middle
cell already contains `U-L` by (1.5).  Hence the covered union is exactly
`L`, the three-middle-cell union is exactly `U`, and all five interval
constraints hold.  This is a canonical physical replay.

Inspection of (2.1) shows that `phi` occurs only through `O_phi(s)` and
`O_phi(u)`.  Since the roots are fixed, (1.1) reduces these to (2.4).
Neither `O_phi(p)` nor a source-token label occurs.  \(\square\)

The source labels are nevertheless required by outer-parent
authentication: after a receiver host is chosen, its real source is fixed
by the inverse outer matching.  The theorem says only that those labels do
not enter the five-cell equation.

## 3. The two phase markers are both genuinely necessary

The reduction to two markers is not reducible to just one on the frozen
data.

### Proposition 3.1 (minimal phase input on `P*`)

Among the `1,748` regenerated records:

* changing only the short marker while keeping the successor marker fixed
  flips validity on `135` records; and
* changing only the successor marker while keeping the short marker fixed
  flips validity on `136` records.

If both markers are unchanged, validity is unchanged on every record.

Explicit witnesses are:

```text
short-marker essential
  ordinal 15
  (s,p,u;q,alpha,beta)=(3327,10071,3792;7,1,0)
  d_0(s),d_1(s)=(32,32768), d_0(u)=d_1(u)=16
  valid=(false,true)

successor-marker essential
  ordinal 8
  (s,p,u;q,alpha,beta)=(487,3325,1223;7,1,0)
  d_0(s)=d_1(s)=16384, d_0(u),d_1(u)=(1,256)
  valid=(false,true).
```

#### Proof

Evaluate the exact predicate (2.2)--(2.3) on the two frozen owner maps.
The audit independently constructs the cells as in the proof of Theorem
2.1 and requires equality of the two verdicts on every tested case.  The
stated counts and witnesses follow.  \(\square\)

Thus the exact mutable owner interface of one fresh ticket consists of two
literal coordinate points.  Treating the owner phase as a single anonymous
bit loses necessary information.

## 4. Fixed-triple flag rigidity

Let `T*` be the regenerated ticket ledger of the inverse parent `P*`.
Token relabelling does not affect this section because tokens are absent
from Theorem 2.1.

### Theorem 4.1 (complete canonical-menu obstruction)

For every one of the `1,748` frozen host triples `(s,p,u)`, exhaust all
`20` reset-monotone choices `(q,alpha,beta)`.  In either owner phase the
valid menu is either empty or the singleton containing the original ticket
choice.  The exact census is

\[
\begin{array}{c|rr}
 &\text{empty menu}&\text{original singleton}\\ \hline
\phi=0&1228&520\\
\phi=1&1247&501.
\end{array}                                                 \tag{4.1}
\]

The two singleton sets have intersection `332`; their differences have
sizes `188` and `169`, and `1,059` triples have empty menus in both phases.
Even allowing a different address/flag choice in each phase therefore gives
a two-phase witness on exactly the same `332` triples as the fixed replay.

#### Proof

There are `69,920` phase/triple/menu cases.  The exact predicate of Theorem
2.1 and the independent constructive replay agree in every case.  Each
nonempty menu is then checked to equal the singleton original choice.  The
set intersections give the remaining counts.  \(\square\)

### Corollary 4.2 (host movement is necessary)

Changing only `q,alpha,beta` repairs none of the `1,228` phase-zero failures
and none of the `1,247` phase-one failures.  Any fresh phase-specific ticket
replacing one of those failed records must change at least one of

\[
                         s,\quad p,\quad u.                  \tag{4.2}
\]

In particular, preservation of the bulk `1,748` host-triple ledger cannot
be interpreted as an `O(1)` flag/reset sidecar on this K17 object.  This is
a finite obstruction to that preservation strategy, not an asymptotic
lower bound and not an obstruction to independently selected phase banks.

## 5. Exact replacement problem and the bounded-state boundary

Theorem 4.1 replaces the failed “same ledger, new flags” idea by an exact
phase-specific host-packing problem.  For each phase `phi`, form a
resource-labelled hypergraph whose edges are all tuples

\[
                 (s,p,u;q,\alpha,\beta)                      \tag{5.1}
\]

satisfying Theorem 2.1.  Attach to `p,u` their unique authenticated inverse
outer sources (or the one declared soft endpoint).  A phase-specific ticket
bank with private shorts, long hosts, and real tokens is exactly a matching
in this expanded hypergraph with the corresponding resource-capacity
constraints.  This is an exact reformulation; existence of the required
matching is **UNPROVED**.

At the flag quotient, a bank `B` exports predecessor and successor counts

\[
 A_i=|\{\tau\in B:\alpha(\tau)=i\}|,
 \qquad B_i=|\{\tau\in B:\beta(\tau)=i\}|,                  \tag{5.2}
\]

and its downward reset vector is

\[
 R_t=\sum_{\tau\in B}{\bf1}\{\beta(\tau)\le t<\alpha(\tau)\}
    =\sum_{i\le t}(B_i-A_i),\qquad 0\le t\le2.              \tag{5.3}
\]

Equation (5.3) is the complete anonymous flag-conservation imbalance.  A
literal direct-arc completion additionally needs the actual endpoint-host
graph; the three numbers alone are not a Hall certificate.

For calibration only, the surviving subsets of the frozen ledger have

\[
 R^{(0)}=(156,0,30),\qquad
 R^{(1)}=(148,0,32),\qquad
 R^{(0\cap1)}=(98,0,22).                                   \tag{5.4}
\]

These are not full banks and (5.4) proves no bounded-reset completion.

The local theorem permits all unexported tickets to be phase-local.  A
claim of only `O(1)` carried connector/reset state must therefore designate
a bounded set of exported occurrences and explicitly transport, for each
one, its actual short/endpoint hosts or a bijection between them, inverse
outer source pins, `q,alpha,beta`, emitted physical cells, endpoint aperture,
and every externally read address/history field.  Bulk existential erasure
does not imply literal host carry.  No bounded exported set or dependency
isomorphism is constructed here; both remain **UNPROVED**.

## 6. Proof boundary

The following statements are **PROVED**:

1. exact equivalence of canonical five-cell replay and (2.2)--(2.3);
2. phase locality through exactly the short and successor owner-extension
   points, with the predecessor owner and token labels absent;
3. necessity of each of the two marker inputs on the frozen K17 data;
4. empty-or-original-singleton menus on all `1,748 x 2` fixed host triples;
5. the resulting necessity of host movement on `1,228/1,247` failed
   records; and
6. the exact phase-specific resource-hypergraph reduction and aggregate
   reset identity (5.3).

The following statements are **UNPROVED**:

1. a matching of size `1,748` in either fresh phase hypergraph;
2. simultaneous private short/long/token capacity and actual-address
   injectivity;
3. a common or bounded-interface pair of phase matchings;
4. directed cycle-cover/reset completion on the literal host graph;
5. endpoint aperture, aggregate history, reset, residence, supplier,
   compiler, and selected `z=6` dependency closure on those fresh banks;
6. any all-`k` clone-good host or regenerative theorem; and
7. every unconditional consequence for `nu(k)`.

## 7. Frozen audit

```text
scratch/audit_k17_pstar_fresh_ticket_local_interface_20260802.py
  SHA-256 b2e2cd3d69b6a99b482acd94e3ba48c17635c6ead4724bb53753c1bde7fe8d3d

scratch/k17_planted_b5_inverse_outer_parent_20260802/
  fresh_ticket_local_interface.audit.json
  SHA-256 5bfb5fcb0e0eb2528947c07506ff10f74cf5c375da5635efffbcf71c8fcefc8f
```

The audit binds the exact host, regenerated ledger, and both s7 owner-phase
hashes.  It checks all owner increments, all `69,920` menu cases by two
equivalent implementations, the exact pass-set census, both marker
essentiality strata, and the reset-vector identity.
