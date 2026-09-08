# K17 occurrence296+C6 common-guard linkage evaluation: fail-closed

Date: 2026-07-31  
Lane: K, common-cap/compiler  
Status: H2/H4-authenticated source-relative checkpoint; upstream physical
failure; no compiler graph or K17 word

## 0. Verdict

The occurrence296 plus 1160-C6 checkpoint is independently authenticated,
but it is not upstream accepted for the compiler.  Its exact gated state is

\[
 (c_{\rm cent},U_{\rm host},w_{\rm up},\mathsf{CC})
       =(0,776,2525,\bot_{\rm phys}).
\tag{0.1}
\]

Here:

* central ownership and the immediate lower palette are exact;
* \(U_{\rm host}=776\) is the exact missing row-bit host mass;
* \(w_{\rm up}=1585+824+116=2525\) is the number of missing upper target
  masks in ranks 10--12; and
* \(\mathsf{CC}=\bot_{\rm phys}\) means that no literal common-guard graph
  exists yet.

Consequently none of

\[
 H_Q,\qquad V_*,\qquad r_Q(A),\qquad\Gamma_\eta
\tag{0.2}
\]

is defined on this checkpoint.  Equivalently, \(V_*=+\infty\) in the
lexicographic fail-closed convention.  The scalar cell ledger and all
marginal provider graphs remain pre-Hall diagnostics, not compiler slack.

## 1. Authenticated subject

The checkpoint composes:

1. the authenticated occurrence_greedy296 macro selection and regenerated
   connected residual flow; and
2. the saved 1160-move residual C6 history on that regenerated fibre.

The primary exact hashes are:

    candidate
    960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c

    canonical final residual
    6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4

    canonical residual payload
    c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4

H2 independently reconstructed every macro and every C6 step:

    checker
    04e0148f4005f96c64df3f88d80628ffc8172e3c7fce67bf8f60e3c3fb1a1b29

    audit JSON
    fc6716d285f774c246e22b7cbfd9a29f69391ace9f7d8089061d2fed57f38be7

    semantic payload
    caef94767d76ef5fab84aa1bba454740c6fcca4e98914ac74ed0615d777a278d

The independent H4 audit agrees:

    audit JSON
    0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4

    semantic payload
    1466d61c961b3343151fa0e84fea2b6a9edce6d8b4bbf498ce751041eef1cc91

This authentication proves exact source-relative reconstruction, one owner
cycle, and the stated ledgers.  It does not mean that physical inversion or
the compiler passes.

## 2. Exact physical data

Both independent replays give:

    rank-nine owners / distinct                    24310 / 24310
    lower-q1 colours / distinct                    24310 / 24310
    maximal-envelope empty / minimum size              0 / 6
    replay mismatch rows                                 748
    missing row-bit host obligations                     776
    strict nonflat D2 / D3                         503 / 503
    upper holes ranks 10 / 11 / 12            1585 / 824 / 116
    upper holes ranks 13 through 17                         0

The strict-D2 packet length profile is

\[
                         1^{230}\,2^{273}.
\tag{2.1}
\]

Therefore its exact lost-bit weight is

\[
                         230+2\cdot273=776.
\tag{2.2}
\]

The mismatch-row support is 748 rather than 776 because one row may miss
more than one coordinate bit.

## 3. Maximal-envelope obstruction

Let \(Z=(Z_i)\) be the proposed depth-two derivative row and let

\[
 E_p=\bigcap_{i:p\in\{i,i+1,i+2\}} Z_i
\tag{3.1}
\]

be its maximal three-window envelope, with the appropriate linear endpoint
truncation.  Every literal inverse word \(Q\) satisfying
\(D^2Q=Z\) must obey

\[
                         Q_p\subseteq E_p.
\tag{3.2}
\]

Hence, for every row,

\[
 D^2Q_i
   =Q_i\cup Q_{i+1}\cup Q_{i+2}
   \subseteq E_i\cup E_{i+1}\cup E_{i+2}.
\tag{3.3}
\]

Define the hard host potential

\[
 U_{\rm host}(Z)
  =\sum_i
    \left|
      Z_i\setminus(E_i\cup E_{i+1}\cup E_{i+2})
    \right|.
\tag{3.4}
\]

### Theorem 3.1 (pre-Hall obstruction)

If every envelope letter is nonempty, then

\[
 U_{\rm host}(Z)=0
 \quad\Longleftrightarrow\quad
 E\text{ literally replays }Z.
\tag{3.5}
\]

If \(U_{\rm host}(Z)>0\), no set word \(Q\subseteq E\) realizes \(Z\).

#### Proof

The forward implication in (3.5) is the definition of zero set difference;
the reverse is immediate.  For the second claim, choose any missing pair
\((i,x)\).  Equation (3.4) says
\(x\notin E_i\cup E_{i+1}\cup E_{i+2}\).  Equation (3.2) then excludes
\(x\) from all three letters of \(D^2Q_i\), while \(x\in Z_i\), contradicting
literal replay.  \(\square\)

The authenticated value \(U_{\rm host}=776>0\) therefore proves

\[
                         \mathcal Q_{\rm phys}(Z)=\varnothing.
\tag{3.6}
\]

The 503 strict short packets are the run-monoid representation of the same
obstruction.  They are useful seam-local repair coordinates, but their
number and weight are not append costs.

## 4. Smallest common-guard state on this checkpoint

For an upstream-accepted chronology, the smallest fixed-sink compiler state
would be

\[
 (Q,M,U,F,r_Q),
\tag{4.1}
\]

where \(Q\) is one literal common guard, \(M\) a transported partial
matching, \(U\) its exposed target bank, \(F\) its free physical-cell sink
bank, and \(r_Q(A)\) the strict-gammoid linkage rank for every future source
subset \(A\subseteq U\).  For one already fixed exposed set, only
\(r_Q(U)\) is needed; pairing-sensitive gluing requires the full oriented
linkage relation.

At the present checkpoint, (3.6) means that the type (4.1) has no inhabitant.
The smallest correct exported value is the distinguished rejecting symbol

\[
                         \boxed{\mathsf{CC}(Z)=\bot_{\rm phys}.}
\tag{4.2}
\]

It is unsound to build a marginal \(H\), take a matching in it, or compute a
gammoid rank and call the result provisional compiler slack.  A cap word can
only delete bits from the maximal envelope and cannot repair (3.4).

## 5. Safe pre-Hall information

The following data may be carried to a physical repair search:

1. the exact 776 labelled row-bit host obligations;
2. the 503 D2 and 503 D3 run packets and their seam-local run states;
3. the exact upper-hole sets in ranks 10--12;
4. the owner/lower-q1 exact factor and transported unaffected incidences;
5. fixed physical boundary cells, switch halos, and locally invariant
   guard incidences; and
6. scoped zero-provider floors inside a declared fixed atlas.

An existential or marginal provider graph can give a **no-go** only when
every permitted physical completion is proved to be a subgraph of it.
A matching in such a relaxation proves nothing.  In particular, the scoped
177 absent residual-provider targets of the occurrence296 fibre are not
the common-cap Hall defect.

## 6. Exact activation sequence

The common-cap linkage theorem becomes live only after one descendant
chronology passes, in order:

1. \(U_{\rm host}=0\) and literal replay at every row;
2. zero forbidden residence packets at the required depth;
3. all declared upper/deep target rows;
4. fixed sockets and prepins;
5. a frozen residual target family and literal physical short-cell bank;
6. a nonempty common-guard family \(\mathcal Q\).

Only then may one form

\[
 V_*=\min_{Q\in\mathcal Q}
       \bigl(|\mathcal T|-\nu(H_Q)\bigr),
\tag{6.1}
\]

choose an optimizing \(Q,M\), and evaluate

\[
 r_Q(A),\qquad
 \Gamma_\eta
   =\max_{A\subseteq U}\bigl(\eta|A|-r_Q(A)\bigr).
\tag{6.2}
\]

Thus the authenticated checkpoint is a strong physical-repair improvement,
but it has not crossed the compiler type boundary.

