# Exact full-arc Farkas exclusion of all C106 \(R=1\) signatures

Date: 2026-07-30  
Lane: A  
Status: **proved, source-relative**

## 1. Scope

This note concerns only the frozen K16 length-eight source and its
211,604-seam direction-coherent catalogue.  The authoritative inputs are

    scratch/k16_len8_source_seam_ledger_20260730.bin
      SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

    scratch/k16_direct_cycle_dual_exact_20260730.audit.json
      SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

No assertion is made about seams outside that catalogue or about the
unrestricted K16 problem.  The conclusion below is stronger than integral
infeasibility: it excludes a full continuous relaxation in which every
high-slack seam remains available fractionally.

Let \(D\) be the 93 frozen defects.  The fifteen price-one lock targets are
partitioned into

\[
\begin{aligned}
G_1&=\{35044,36935,40066\},&
G_2&=\{37320,41102,47364\},\\
G_3&=\{33906,36417,51235\},&
G_4&=\{33337,50976,58385\},\\
G_5&=\{41872,49436,61960\}.&&
\end{aligned}                                                   \tag{1.1}
\]

Write \(L=\bigcup_iG_i\) and \(D_0=D\setminus L\), so \(|D_0|=78\).

## 2. The common \(R=1\) lock hull

For a fixed \(R=1\) signature, one lock group carries the slack symbol
‘S’; each of the other four groups has exactly one repeated target.  Its
lock-service vector \(p\) therefore satisfies

\[
 p_t\ge1,\qquad
 \sum_{t\in G_i}p_t\le4\quad(i\in[5]),\qquad
 \sum_{t\in L}p_t=19.                                  \tag{2.1}
\]

### Lemma 2.1 (exact lock convex hull)

The polytope (2.1) is exactly the convex hull of the 405 fixed \(R=1\)
lock-demand vectors.

#### Proof

Put \(y_t=p_t-1\) and

\[
 z_i=1-\sum_{t\in G_i}y_t.
\]

Then \(y_t,z_i\ge0\) and

\[
 z_i+\sum_{t\in G_i}y_t=1,
 \qquad \sum_i z_i=1.                                  \tag{2.2}
\]

Choose the ‘S’ group to be \(i\) with probability \(z_i\).  Conditional on
group \(j\) not being ‘S’, choose its repeated target \(t\in G_j\) with
probability \(y_t/(1-z_j)\); the choice is immaterial if \(z_j=1\).  The
marginal probability of repeating \(t\in G_j\) is \(y_t\).  Hence every
point of (2.1) is a convex combination of fixed signatures.  The reverse
inclusion is immediate. \(\square\)

The certificate below uses only the last equation of (2.1), so it excludes
a larger set than this convex hull.

## 3. Exact cycle-eligibility reduction

For a seam \(e:u\to v\), let \(H(e)\subseteq D\) be its serviced defects and
let

\[
 s(e)=2+\phi_v-\phi_u-\sum_{t\in H(e)}w_t\ge0           \tag{3.1}
\]

be its exact direct-dual slack.  Call \(e\) cycle-eligible when it belongs
to a directed cycle of the full seam graph.  Exactly 211,469 seams are
cycle-eligible and 135 are not.

### Lemma 3.1 (balanced nonnegative flow uses only cycle arcs)

Every nonnegative balanced seam flow vanishes on the 135 cycle-ineligible
seams.

#### Proof

Fix a positive arc \(e:u\to v\), and let \(W\) be the vertices reachable
from \(v\) in the positive-support digraph.  If \(u\notin W\), no positive
arc leaves \(W\), whereas \(e\) enters \(W\).  Summing balance over \(W\)
gives a contradiction.  Thus \(v\) reaches \(u\), and \(e\) lies on a
directed cycle. \(\square\)

This is the only arc deletion used.  In particular, no seam is removed
because \(s(e)>1\).

## 4. Frozen integer certificate

The exact certificate consists of integer port multipliers \(\pi_v\),
integer target multipliers \(\lambda_t\) for \(t\in D_0\), and

\[
 L=816{,}110,\qquad N=-227{,}974,\qquad Q=-558{,}866.   \tag{4.1}
\]

The complete sparse table is frozen in

    scratch/k16_floor106_r1_full_exact_farkas_20260730.audit.json
      SHA-256 d6036de330e46c37886caf549f67d81b5ee13652068288a87899be59b8c69629
      payload  8b7f30a678eff1fd3a5756101f06706b2ba2a416efaa9bbdf9d8848356b361e7

There are 3,509 nonzero port multipliers and 78 nonzero target
multipliers.  For every cycle-eligible seam define

\[
 c(e)=\pi_u-\pi_v
      +\sum_{t\in H(e)\cap D_0}\lambda_t
      +L\,|H(e)\cap L|+N+Q\,s(e).                     \tag{4.2}
\]

### Proposition 4.1 (exact finite inequalities)

For all 211,469 cycle-eligible seams,

\[
                         c(e)\le-1,                    \tag{4.3}
\]

while

\[
 \sum_{t\in D_0}\lambda_t+19L+106N+Q
 =245{,}524>0.                                        \tag{4.4}
\]

#### Proof

The frozen exactifier evaluates every quantity in integers.  Starting from
the numerical ray scaled by 1,000, nearest-integer rounding leaves maximum
column coefficient \(1\); decreasing the free count multiplier by \(2\)
makes the maximum \(-1\), the minimum \(-4{,}238{,}627\), and leaves the
positive right side (4.4).

The exact source bytes used to create the artifact are preserved as

    scratch/exactify_k16_floor106_r1_full_farkas_frozen_74afb25d_20260730.py
      SHA-256 74afb25d926f8ac2feb1638b0009c88cb839393808b70b4b535053c6beaea530

An independent verifier implements its own iterative Kosaraju SCC
decomposition and recomputes all 211,604 seam rows using integer arithmetic:

    scratch/audit_threadA_k16_floor106_r1_full_exact_farkas_20260730.py
      SHA-256 dd4240b1ac1197aeeb39514b5a0865ea76177365486766140d137c7cfd25c23a

    scratch/threadA_k16_floor106_r1_full_exact_farkas_independent_20260730.audit.json
      SHA-256 09277dee302f9d80df8878469ed135b00cf81332dec8ed0cfc7f75dd07ed89ab
      payload  4d1906e73a92af668391b503733dbda596f50c9196046b70c5ee795c6c3dabab

It reproduces (4.3), (4.4), and coefficient-histogram hash
e324238e258aff3aeed84a14b6b433ec2e54e2fde51f4d6ff0ac24163e9a6e7a.
Thus no floating-point inference remains. \(\square\)

## 5. Main theorem

### Theorem 5.1 (all 405 \(R=1\) signatures are impossible)

There is no nonnegative balanced seam flow \(x\) satisfying

\[
\begin{aligned}
 \sum_e h_e(t)x_e&=1 &&(t\in D_0),\\
 \sum_e |H(e)\cap L|x_e&=19,\\
 \sum_e x_e&=106,\\
 \sum_e s(e)x_e&=1.
\end{aligned}                                         \tag{5.1}
\]

Consequently the full continuous common relaxation of all 405 \(R=1\)
signatures is empty.  In particular, no integral capacity-one circulation
realizes an \(R=1\) signature.

#### Proof

By Lemma 3.1, only cycle-eligible seams can be positive.  Multiply the port
balance rows by \(\pi_v\), the 78 nonlock service equations by \(\lambda_t\),
the lock-total equation by \(L\), the count equation by \(N\), and the slack
equation by \(Q\).  Equations (5.1) make the resulting right side equal to
\(245{,}524\).  The left side is

\[
             \sum_e c(e)x_e\le-\sum_e x_e=-106,       \tag{5.2}
\]

by (4.3) and \(x_e\ge0\), a contradiction.  Every fixed \(R=1\) signature
satisfies (5.1).  Notice that no port-capacity, individual lock-lower, or
lock-group inequality was used. \(\square\)

## 6. Exact boundary

Within the frozen source-relative catalogue, \(R=0\) and \(R=1\) are
excluded exactly.  The remaining normal-form counts are

\[
 270+90+15+1=376
\]

for \(R=2,3,4,5\), respectively.  The theorem neither excludes any of those
signatures nor constructs a physical C106 carrier.

The same multiplier table has right-hand-side values

\[
\begin{array}{c|rrrr}
R&1&2&3&4\\ \hline
\mathrm{RHS}_R&245{,}524&-1{,}129{,}452&-2{,}504{,}428&-3{,}879{,}404
\end{array}                                            \tag{6.1}
\]

because lock total is \(20-R\) and slack is \(R\).  Thus this exact ray
stops sharply at \(R=1\); R2--R4 require target-sensitive separators or a
construction.

## 7. Adversarial audit

1. **Full arcs.** Every seam enters the SCC computation, and every
   cycle-eligible seam enters (4.3), irrespective of slack.
2. **No hidden capacity assumption.** Capacity multipliers are zero; the
   contradiction holds after deleting capacity.
3. **Union versus averaging.** The proof needs only the lock-total equation
   common to all fixed signatures.  Lemma 2.1 separately verifies the stated
   convex-hull interpretation.
4. **Exactness.** The numerical ray is only provenance.  The theorem rests
   on the frozen integer table and the independent integer replay.
5. **Scope.** This is a source-relative balanced/service theorem.  It is not
   an unrestricted K16 impossibility theorem or a physical-word theorem.
